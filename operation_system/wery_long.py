"""
Самая длинная строка в файле. Если строк такой длины несколько, то первую, которая встретилась в файле.
"""

filename = input()  # 'zen.txt'
with open(filename, 'r', encoding='utf-8') as f:
    file_lst = f.readlines()

maxlen = ''
for fl in file_lst:
    if len(maxlen) < len(fl.strip()):
        maxlen = fl.strip()
        
print(maxlen)
