"""
Подсчитать, сколько строк начинается на букву П
"""

filename = input()  # 'zen.txt'
with open(filename, 'r', encoding='utf-8') as f:
    file_lst = f.readlines()

count = 0
for fl in file_lst:
    if fl.startswith('П'):
        count +=1 
        
print(count)
