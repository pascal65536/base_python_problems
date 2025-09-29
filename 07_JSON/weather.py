'''
Вывести погоду сегодня, завтра и послезавтра. 
В градусах Цельсия и описание осадков или погоды.

https://wttr.in/KJA?format=j1

Можно заменить KJA на название города по-английски и получить прогноз в другом населенном пункте
'''

import json

with open('krasnoyarsk.json', 'r', encoding='utf-8') as f:
    city_dct = json.load(f)

result = list()
for weather in city_dct.get('weather', list()):
    local_dct = dict()
    local_dct['avg_temp'] = weather.get('avgtempC')
    local_dct['date'] = weather.get('date')
    for hourly in weather.get('hourly', list()):
        weather_desc = hourly.get('weatherDesc')
        for name_snow in weather_desc:
            local_dct['name_snow'] = name_snow.get('value')
        break
    result.append(local_dct)


for r in result:
    print(r['date'], r['avg_temp'], r['name_snow'])

