# coding=utf-8
import httplib
import urllib
import json
import time

# https://geocode-maps.yandex.ru/1.x/?format=json&geocode=Тверская+6.
conn = httplib.HTTPSConnection("geocode-maps.yandex.ru")

output_file = open('output.csv', 'w')

with open('input2.csv', 'r') as input_file:
    next(input_file)  # skip first line
    line_number = 2
    for input_line in input_file:
        cells = input_line.split(';')
        if len(cells) > 1:
            if len(cells[0]) > 0 and len(cells[1]) > 0:
                address = cells[0] + ' ' + cells[1]
                address_encoded = urllib.quote(address)

                conn.request("GET", "/1.x/?format=json&results=1&geocode=" + address_encoded)
                resp = conn.getresponse()
                # print resp.status, resp.reason
                if resp.status == 200:
                    json_resp = json.loads(resp.read())
                    try:
                        coord_str = json_resp[u'response'][u'GeoObjectCollection'][u'featureMember'][0][u'GeoObject'][u'Point'][u'pos']
                        output_file.write(coord_str + '\n')
                        print coord_str
                    except:
                        print 'Something wrong with format of geocoder response for line', line_number
                else:
                    print 'Error occured during request for address', address, 'at line', line_number

            else:
                print 'Street name or building number is empty at line', line_number
        else:
            print 'Not enough data in line', line_number
        #time.sleep(0.05)
        line_number += 1

output_file.close()

