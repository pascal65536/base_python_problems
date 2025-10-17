### Что такое «RAG» и зачем нужны несколько файлов

**RAG** – *Retrieval‑Augmented Generation*.  
Это подход, при котором генеративная модель (LLM) получает к своему ответу не только токены из запроса, но и релевантные фрагменты из внешнего источника знаний (текстовых документов, баз данных, веб‑страниц и т.д.).  

Чтобы реализовать RAG вам нужно:

1. **Импортировать все документы** в память (или векторный индекс).  
2. При запросе сформировать **вектор запроса**, найти ближайшие к нему документы (или их части) – это «retrieval»‑шаг.  
3. Сгенерировать ответ, включив найденные фрагменты как контекст – это «generation»‑шаг.

Ниже приведены пошаговые инструкции и готовые примеры для **Python** с использованием самых популярных библиотек:

- `langchain` (платформа для RAG).  
- `faiss` / `pinecone` (для векторного поиска).  
- `sentence-transformers` или `OpenAI embeddings`.

---

## 1. Установка зависимостей

```bash
pip install langchain faiss-cpu sentence-transformers openai tiktoken
# Если хотите использовать Pinecone:
# pip install pinecone-client
```

> **Tip** – если у вас GPU, замените `faiss-cpu` на `faiss-gpu`.

---

## 2. Подготовка файлов

Допустим, у нас есть несколько текстовых файлов в папке `data/`:

```
data/
├── article1.txt
├── report2.pdf          # pdf‑файлы можно конвертировать в txt
├── notes.md
└── summary.docx        # docx → txt
```

### 2.1 Преобразуем все файлы в строки

```python
import os
from pathlib import Path
import textract  # pip install textract (для pdf, docx и т.п.)

DATA_DIR = Path("data")

def load_text_from_file(path: Path) -> str:
    return textract.process(str(path)).decode('utf-8')

documents = []
for file_path in DATA_DIR.iterdir():
    if file_path.suffix.lower() in {".txt", ".pdf", ".md", ".docx"}:
        documents.append(load_text_from_file(file_path))
```

> `textract` умеет читать PDF, DOCX, PPT и т.д.  
> Если хотите разбить большие файлы на чанки – используйте `langchain.text_splitter`.

### 2.2 Разбиваем на чанки

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents([{"page_content": d} for d in documents])
# Теперь `chunks` – список dict‑ов с полем page_content
```

---

## 3. Создание векторного индекса

### 3.1 Векторизуем чанки (embeddings)

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()          # использует OpenAI API
# Если хотите использовать local model:
# from sentence_transformers import SentenceTransformer
# embeddings = SentenceTransformer('all-MiniLM-L6-v2')
```

### 3.2 Создаём FAISS‑индекс

```python
import faiss
import numpy as np

def embed_chunks(chunks):
    texts = [c["page_content"] for c in chunks]
    vecs = embeddings.embed_documents(texts)
    return np.array(vecs).astype('float32')

vectors = embed_chunks(chunks)

index = faiss.IndexFlatL2(vectors.shape[1])   # L2‑distance
index.add(vectors)                           # индексируем

# Сохраняем, чтобы не пересоздавать каждый запуск:
faiss.write_index(index, "data/faiss.idx")
```

> Для больших наборов используйте `IndexIVFFlat` или `Pinecone`.

---

## 4. RAG‑pipeline (объединение Retrieval + Generation)

```python
from langchain.llms import OpenAI   # LLM‑модель
from langchain.chains import RetrievalQA

llm = OpenAI(temperature=0)          # или ChatOpenAI, Gemini, Claude и т.д.

# Функция для поиска в FAISS
def retrieve(query: str, k=5):
    q_vec = embeddings.embed_query(query).astype('float32')
    D, I = index.search(np.array([q_vec]), k)
    return [chunks[i]["page_content"] for i in I[0] if i < len(chunks)]

# Создаём цепочку
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",          # «stuff» – просто склеивает контекст и передаёт в LLM
    retriever=retrieve,          # пользовательский `retriever`
)

def ask(query: str):
    return qa_chain.run(query)

# Пример использования:
print(ask("Что такое RAG?"))
```

> Если вы используете LangChain v0.2+, можно заменить `RetrievalQA` на более гибкие цепочки (`LLMChain`, `ConversationChain`) и задать собственный формат вывода.

---

## 5. Полностью готовый скрипт

```python
# rag_from_files.py
import os, faiss, numpy as np
from pathlib import Path
import textract
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

DATA_DIR = Path("data")
INDEX_FILE = "data/faiss.idx"

# ---------- 1. Загрузка файлов ----------
def load_text_from_file(path: Path) -> str:
    return textract.process(str(path)).decode('utf-8')

documents = [load_text_from_file(p)
             for p in DATA_DIR.iterdir()
             if p.suffix.lower() in {".txt", ".pdf", ".md", ".docx"}]

# ---------- 2. Разбиваем на чанки ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents([{"page_content": d} for d in documents])

# ---------- 3. Векторизуем и индексируем ----------
embeddings = OpenAIEmbeddings()
vectors = np.array(embeddings.embed_documents([c["page_content"] for c in chunks])).astype('float32')

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)
faiss.write_index(index, INDEX_FILE)

# ---------- 4. Создаём RAG‑цепочку ----------
llm = OpenAI(temperature=0)

def retrieve(query: str, k=5):
    q_vec = embeddings.embed_query(query).astype('float32')
    D, I = index.search(np.array([q_vec]), k)
    return [chunks[i]["page_content"] for i in I[0] if i < len(chunks)]

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retrieve
)

# ---------- 5. Пример запроса ----------
if __name__ == "__main__":
    while True:
        q = input("\nВведите вопрос (или 'выход'): ")
        if q.lower() in {"выход", "quit", "exit"}: break
        print("\nОтвет:\n", qa_chain.run(q))
```

> Запустите `python rag_from_files.py`. Введите любой вопрос – модель сначала найдет релевантные фрагменты из ваших файлов, а затем сгенерирует ответ.

---

## 6. Что делать дальше?

| Что хотите сделать | Как продвинуться |
|--------------------|-----------------|
| **Обучить LLM** на ваших данных (fine‑tune) | Используйте `HuggingFaceHub` + `datasets`, или сервисы вроде `OpenAI Fine-tuning`. |
| **Мульти‑модальные данные** (текст + изображения) | Добавьте векторизацию изображений через CLIP, объедините с текстом. |
| **Постоянный индекс** (не пересоздавать каждый раз) | Сохраняйте `faiss.idx` и загружайте его (`faiss.read_index`). |
| **Кэширование запросов** | Встроенные в LangChain кеши (`Memory`, `Cache`) или внешние решения. |
| **Интерфейс веб‑чат** | FastAPI + Streamlit / Gradio, подключив ваш RAG‑pipeline как API. |

---

### Быстрый чеклист

1. Установить зависимости.  
2. Считать все файлы (используйте `textract` для PDF/Docx).  
3. Разбить на чанки (`RecursiveCharacterTextSplitter`).  
4. Векторизовать чанки (OpenAIEmbeddings или local модель).  
5. Создать FAISS‑индекс и сохранить его.  
6. Написать функцию `retrieve(query)`, которая возвращает ближайшие фрагменты.  
7. Объединить `retrieve` с LLM через LangChain (`RetrievalQA`).  
8. Запустить