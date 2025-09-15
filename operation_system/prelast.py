with open(input(), 'r', encoding='utf-8') as f:
    filestr = f.readlines()

print(filestr[-2].strip())
