import random


def generate(count=10):
    i = 0
    random_lst = list()
    while i < count:
        random_lst.append(random.randint(0, 100))
        i += 1
    return random_lst


if __name__ == "__main__":
    ret = generate()
    print(ret)
    ret = generate(20)
    print(ret)
