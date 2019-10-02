# Fixes a problem in the previous version of the code.

import requests, datetime

countries = [84, 188, 192, 222, 320, 332, 340, 484, 558, 591, 214]

now = datetime.datetime.now()
current_year = now.year

for country in countries:
    print('Country: ' + str(country))
    for i in range(1990,current_year):
        for x in range(0,2):
            request = requests.get('http://comtrade.un.org/api/get/bulk/C/A/' + str(i) + '/' + str(country) + '/HS?token=mysecrettoken')
            if request.status_code == 200: # A status code of 200 indicates success.
                print('Year ' + str(i) + ' successful.')
                with open('C:/Users/ljuskelis/Desktop/UN Comtrade2/' + str(country) + '.' + str(i) + '.zip', 'wb') as file:
                    file.write(request.content)
                break
            else:
                print('Year ' + str(i) + ' NOT successfully loaded on try number ' + str(x) + '.')

print('Done.')

