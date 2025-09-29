import requests
import json

urls = [
    "https://stepik.org/media/attachments/course/235849/cars.json", 
    "https://stepik.org/media/attachments/course/235849/flights.json",
    "https://stepik.org/media/attachments/course/235849/library.json",
    "https://stepik.org/media/attachments/course/235849/store.json",
    "https://stepik.org/media/attachments/course/235849/product.json"
    ]

for url in urls:
    response = requests.get(url)
    data = response.json()
    filename = filename = '_' + url.split('/')[-1]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)        