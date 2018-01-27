# coding=utf-8
import httplib
import urllib
import json
import time

# https://geocode-maps.yandex.ru/1.x/?format=json&geocode=Тверская+6.
conn = httplib.HTTPSConnection("geocode-maps.yandex.ru")

output_file = open('output.csv', 'w')
errors_file = open('errors.log', 'w')

def errorMessage(err_file, addr, line, message):
    msg = 'line ' + str(line) + ' <' + addr + '> - ' + message
    print msg
    err_file.write(msg + '\n')

def checkLongitude(longitude):
    western_limit = 29.0 # Чуть западнее Соснового Бора
    eastern_limit = 31.1 # Чуть восточнее Шлиссельбурга
    return (longitude > western_limit) and (longitude < eastern_limit)

def checkLatitude(latitude):
    northern_limit = 60.15 # Чуть севернее Сертолово
    southern_limit = 59.5  # Чуть южнее Гатчины
    return (latitude > southern_limit) and (latitude < northern_limit)

def checkCoordString(str):
    tokens = str.split(' ');
    if len(tokens):
        try:
            longitude = float(tokens[0])
            latitude  = float(tokens[1])
        except:
            return False;
        return checkLongitude(longitude) and checkLatitude(latitude)
    else:
        return False

with open('input3.csv', 'r') as input_file:
    next(input_file)  # skip first line
    line_number = 2
    for input_line in input_file:
        cells = input_line.split(';')
        if len(cells) > 1:
            action_point = cells[0].translate(None, ' \n\t\r')
            address = cells[1].translate(None, ' \n\t\r')
            if len(address) > 0:
                address_encoded = urllib.quote(address)

                conn.request("GET", "/1.x/?format=json&results=1&geocode=" + address_encoded)
                resp = conn.getresponse()
                if resp.status == 200:
                    json_resp = json.loads(resp.read())
                    try:
                        coord_str = json_resp[u'response'][u'GeoObjectCollection'][u'featureMember'][0][u'GeoObject'][u'Point'][u'pos']
                        if (checkCoordString(coord_str)):
                            output_file.write(coord_str + ' ')
                            output_file.write(action_point + '\n')
                            print coord_str, action_point
                        else:
                            errorMessage(errors_file, address, line_number, 'wrong coordinates - ' + coord_str)
                    except:
                        errorMessage(errors_file, address, line_number, 'something wrong with format of geocoder response')
                else:
                    errorMessage(errors_file, address, line_number, 'error occured during HTTP request, code ' + str(resp.status))
            else:
                errorMessage(errors_file, '?', line_number, 'address is empty')
        else:
            errorMessage(errors_file, '?', line_number, 'not enough data')
        line_number += 1

output_file.close()
errors_file.close()

