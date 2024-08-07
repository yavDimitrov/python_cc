from copy import deepcopy

info_bike = {
    'name': 'Cross',
    'model': 'GRX8',
    'rides': []
}

new_info_bike = deepcopy(info_bike)

new_info_bike['rides'].append(58)

print(info_bike)

print(new_info_bike)
