word = 'Мама мыла раму'
new = ''
for char in word:
    if char == ' ':
        continue
    new = new + char
# print(new)

for char in word:
    if char == ' ':
        continue
    print(char * 6)
