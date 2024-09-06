car_dct = {
    "Toyota": {"model": "Premio", "year": 2013, "sale": 1100},
    "Lada": {"model": "Kalina", "year": 2014, "sale": 420},
    "Mersedes": {"model": "G", "year": 2020, "sale": 3000},
    "UAZ": {"model": "Patriot", "year": 2019, "sale": 1247},
    "BMW": {"model": "G21", "year": 2022, "sale": 5400},
    "Mazda": {"model": "Familia", "year": 2002, "sale": 200},
    "Ford": {"model": "Mondeo", "year": 2010, "sale": 615},
}

for num, (car_name, model_dct) in enumerate(car_dct.items()):
    print(num)
    print(car_name)
    print(model_dct)

car_dct = {
    "brand": "Toyota",
    "model": "Premio",
    "year": 2013,
    "sale": 1100,
    "color": "Red",
}

market_lst = [
    {"brand": "Toyota", "model": "Premio", "year": 2013, "sale": 1100, "color": "Red"},
    {"brand": "Lada", "model": "Kalina", "year": 2014, "sale": 420, "color": "Black"},
    {"brand": "Mercedes", "model": "G", "year": 2020, "sale": 3000, "color": "Gray"},
    {"brand": "UAZ", "model": "Patriot", "year": 2019, "sale": 1247, "color": "Orange"},
    {"brand": "BMW", "model": "G21", "year": 2022, "sale": 5400, "color": "White"},
    {"brand": "Mazda", "model": "Familia", "year": 2002, "sale": 200, "color": "Green"},
    {"brand": "Ford", "model": "Mondeo", "year": 2010, "sale": 615, "color": "Yellow"},
]

list_dict = [{}, {}, {}]


# Количество автомобилей, выставленных на продажу
print(len(market_lst))

# Создать список автомобилей дешевле 2000
# Создать список автомобилей старше 2015 года
lowprice_lst = list()
oldcar_lst = list()
for car_dct in market_lst:
    print(car_dct["brand"], car_dct["model"])
    if car_dct["sale"] <= 2000:
        lowprice_lst.append(car_dct)
    if car_dct["year"] <= 2015:
        oldcar_lst.append(car_dct)

print(lowprice_lst)
print(oldcar_lst)
