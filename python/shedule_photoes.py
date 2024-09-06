from itertools import cycle
import random

schedule_peoples = {
    'K': {
        '2024-05-15': [
            range(11, 14)
        ],
        '2024-05-16': [
            range(10, 14)
        ],
    },
    'P': {
        '2024-05-15': [
            range(12, 14)
        ],
    },
    'I': {
        '2024-05-15': [
            range(14, 16)
        ],
    },
    'D': {
        '2024-05-15': [
            range(15, 17)
        ],
        '2024-05-16': [
            range(15, 17)
        ],
    },
    'A': {
        '2024-05-15': [
            range(15, 17),
            range(17, 19)
        ],
        '2024-05-16': [
            range(15, 17)
        ],
    },
    'F': {
        '2024-05-16': [
            range(10, 12),
            range(15, 17)
        ],
    },
}


def his_can(schedule_peoples, person, day, hour):
    hours_range_lst = schedule_peoples.get(person, dict()).get(day, list())
    for hours_range in hours_range_lst:
        if hour in hours_range:
            return True
    return False


def find_available_time(schedule_peoples, person):
    available_time = []
    for day, hours in schedule_peoples[person].items():
        for hour_range in hours:
            for hour in hour_range:
                available_time.append((day, hour))
    return available_time


person_result = dict()
shedule_result = dict()

for day in ['2024-05-15', '2024-05-16']:
    for hour in range(10, 19):
        if (day, hour) in shedule_result:
            continue
        for person in schedule_peoples:
            if person in person_result:
                continue
            if his_can(schedule_peoples, person, day, hour):
                person_result.update({
                    person: (day, hour)
                })
                shedule_result.update({
                    (day, hour): person
                })
                break
    if (day, hour) in shedule_result:
        continue
    if person in person_result:
        break

import pprint

pprint.pprint(person_result)
pprint.pprint(shedule_result)
sorted_dict = dict(sorted(person_result.items(), key=lambda x: (x[1][1], x[1][0])))
print(sorted_dict)
