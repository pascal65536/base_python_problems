a = int(input())
b = int(input())
d = len(str(a * b))
for i in range(1, a + 1):
    ll = list()
    for j in range(i, (a * b) + 1, a):
        ll.append(f"{j: <{d}}")
    ss = " ".join(ll).strip()
    print(ss)
