"""     
     1     
    2 3    
   4 5 6   
 7 8 9 10  
11 12 13 14
"""


def slice(start, tail):
    i = 1
    while len(" ".join(tail[:i])) <= len(start):
        i += 1
    return " ".join(tail[:i]), tail[i:]


num = int(input())
if not num:
    exit()
start_lst = ["1"]
ls = [str(x) for x in range(2, num + 1)]

while len(" ".join(ls)) > len(start_lst[-1]):
    body, tail = slice(start_lst[-1], ls)
    start_lst.append(body)
    ls = tail
if ls:
    start_lst.append(" ".join(ls))

maxlen = len(max(start_lst, key=len))
for s in start_lst:
    print(f"{s: ^{maxlen}}")
