import json
from pprint import pprint as print

dct = {
    False: 'False',
    True: 'True',
    2: 'two',
    4: 'four',
    None: 'None',
    'is_alpha': True,
    'is_digit': False,
    'is_lower': None,
    '1, 2, 3': 'tuple',
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'JS', 'CSS', 'HTML'],
}

print(dct)

# one = json.dumps(dct)
# print(one, type(one))

# two = json.loads(json.dumps(dct))
# print(two, type(two))

with open('dct.json', 'w', encoding='utf-8') as f:
    json.dump(dct, f, ensure_ascii=False, indent=4)

with open('dct.json', 'r', encoding='utf-8') as f:
    three = json.load(f)

print(three)