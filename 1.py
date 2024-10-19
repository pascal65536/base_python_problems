import string


def dec_to_any(num, radix):
    res = ""
    alphabet = string.digits + string.ascii_uppercase
    while num > 0:
        res = f"{alphabet[num % radix]}{res}"
        num = num // radix
    return res


print(dec_to_any(123456789, 2))
print()
print(dec_to_any(123456789, 10))
