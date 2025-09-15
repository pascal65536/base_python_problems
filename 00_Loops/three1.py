"""     
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
"""

num = input()
start_lst = list()
ls = [x for x in range(1, num + 1)]
i = 1
while len(ls) > 0:
    head = ls[:i]
    tail = ls[i:]
    i += 1
    start_lst.append(head)
    ls = tail

start_lst = [' '.join(list(map(str, x))) for x in start_lst]
maxlen = len(max(start_lst, key=len))
for s in start_lst:
    print(f"{s: ^{maxlen}}")
