scrabble_dict = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "Й": 4,
    "К": 2,
    "Л": 2,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 2,
    "Ф": 10,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3,
}

# print(scrabble_dict)
# res = scrabble_dict['А']
# print(res)

# for i in scrabble_dict.items():
#     if i[1] == 5:
#         print(i[0])

# for k, v in scrabble_dict.items():
#     if v == 5:
#         print(k)


car_dct = {
    "Toyota": {"model": "Premio", "year": 2013, "sale": 1100},
    "Lada": {"model": "Kalina", "year": 2014, "sale": 420},
    "Mersedes": {"model": "G", "year": 2020, "sale": 3000},
    "UAZ": {"model": "Patriot", "year": 2019, "sale": 1247},
    "BMW": {"model": "G21", "year": 2022, "sale": 5400},
    "Mazda": {"model": "Familia", "year": 2002, "sale": 200},
    "Ford": {"model": "Mondeo", "year": 2010, "sale": 615},
}

for car_name, model_dct in car_dct.items():
    if model_dct["year"] >= 2020:
        print(car_name)

# вывести список автомобилей, стоимость которых меньше 1000
# найти самый дешевый автомобиль, показать его название, год выпуска и цену


lowcost = list(car_dct.keys())[0]
lowcost_sale = car_dct[lowcost]["sale"]
for car_name, model_dct in car_dct.items():
    if model_dct["sale"] < lowcost_sale:
        lowcost = car_name
        lowcost_sale = model_dct["sale"]

print(lowcost, car_dct[lowcost])


# print(lowcost)
# car_dct[lowcost]['model']
# car_dct[lowcost]['year']
# car_dct[lowcost]['sale']
# res = f"Название {lowcost} {car_dct[lowcost]['model']} Год выпуска: {car_dct[lowcost]['year']} Цена: {car_dct[lowcost]['sale']}"
