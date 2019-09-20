# This version incorporates a loop for accessing multiple countries. 

import requests, datetime

countries = [188, 192, 222, 320, 332, 340, 484, 558, 591, 214]

c = 84  # Specify country code.

now = datetime.datetime.now()
current_year = now.year

for country in countries:
    print('Country: ' + str(country))
    for i in range(1990, current_year):
        request = requests.get('http://comtrade.un.org/api/get/bulk/C/A/' + str(i) + '/' + str(country) + '/HS?token=mysecrettoken')
        if request.status_code != 200:
            print('Year ' + str(i) + ' NOT successful.')
        else:
            print('Year ' + str(i) + ' successful.')
            with open('C:/Users/ljuskelis/Desktop/UN Comtrade/' + str(country) + '.' + str(i) + '.zip', 'wb') as file:
                file.write(request.content)

print('Done.')

