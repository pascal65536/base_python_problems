num = int(input())
for i in range(1, num):
    sub = f"*{'!':.^{i * 2 - 1}}*"
    print(f"{sub:-^{num*2-1}}")