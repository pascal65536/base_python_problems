a = 0
b = 1
i = 1
while i < 1000:
    print(i, end=" ")
    i = a + b
    a = b
    b = i
print()
