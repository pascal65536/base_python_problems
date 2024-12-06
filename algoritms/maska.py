from fnmatch import fnmatch

word = "123456789"
res = fnmatch(word, "1[02468]3*6?8[!123456780]")
print(res, word)
