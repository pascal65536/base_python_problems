def number_base(num, radix=10):
    alphabet = "0123456789ABCDEFGH"
    ret = ""
    while num > 0:
        head = num // radix
        ret = f"{alphabet[num % radix]}{ret}"
        num = head
    return ret


num = int(input())

radix_lst = list()
for rad in range(2, 11):
    nb = number_base(num, rad)
    radix_lst.append((sum(list(map(int, nb))), -1 * rad, nb))

print(-1 * max(radix_lst)[1])
