# Converting to json document according to specification
# https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/ObjectManager-docpage/

import json

yandex_json = {'type': 'FeatureCollection', 'features': []}

with open('output.txt', 'r') as input_file:
    index = 0
    action_points = set()
    for line in input_file:
        tokens = line.split(';')
        action_point = tokens[1]
        coord_str = tokens[0]
        action_points.add(action_point)

        tokens = coord_str.split(' ')
        longitude = float(tokens[0])
        latitude  = float(tokens[1])
        json_entry = {'type':'Feature',
                      'id':index,
                      'geometry':
                          {'type':'Point',
                           'coordinates':[latitude, longitude]}}
        yandex_json['features'].append(json_entry)
        index += 1

output_file = open('points-for-yandex.json', 'w')
json.dump(yandex_json, output_file, indent=False)
output_file.close()