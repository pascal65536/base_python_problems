import random
import string

"""
Написать генератор паролей длиной n. Пароль должен состоять из маленьких, 
больших букв латинского алфавита, цифр и знаков пунктуации.
И содержать хотя бы по одному символу из каждого множества.
"""

n = 16
dg = random.randint(1, n - 3)
dg_lst = [random.choice(string.digits) for _ in range(dg)]
al = random.randint(1, n - 2 - dg)
al_lst = [random.choice(string.ascii_lowercase) for _ in range(al)]
au = random.randint(1, n - 1 - dg - al)
au_lst = [random.choice(string.ascii_uppercase) for _ in range(au)]
pn = n - dg - al - au
pn_lst = [random.choice(string.punctuation) for _ in range(pn)]
char_lst = dg_lst + au_lst + al_lst + pn_lst
random.shuffle(char_lst)
print("".join(char_lst))
