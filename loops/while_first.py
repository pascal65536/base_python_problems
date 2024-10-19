# count = 0
# number = int(input())
# while number != 0:
# 	if number % 10 == 2:
# 		count += 1
# 	number = int(input())
# print('Количество искомых чисел:', count)


biggest_book = 0
n = int(input())
while n > 0:
	if biggest_book < n:
		biggest_book = n
	n = int(input())
print(biggest_book)