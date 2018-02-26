# Converting to json document according to specification
# https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/ObjectManager-docpage/

import json
from get_colors import get_colors

yandex_json = {'type': 'FeatureCollection', 'features': []}

with open('output.txt', 'r') as input_file:
    index = 0
    for line in input_file:
        tokens = line.split(';')
        action_point = tokens[1]
        action_point = action_point.strip('\n\r')
        coord_str = tokens[0]

        tokens = coord_str.split(' ')
        longitude = float(tokens[0])
        latitude  = float(tokens[1])
        json_entry = {'type':'Feature',
                      'id':index,
                      'geometry':
                          {'type':'Point',
                           'coordinates':[latitude, longitude]},
                      'properties': {'hintContent': action_point},
                      'options': {'iconColor': get_colors(action_point) }}
        yandex_json['features'].append(json_entry)
        index += 1

output_file = open('points-for-yandex.json', 'w')
json.dump(yandex_json, output_file, indent=False)
output_file.close()