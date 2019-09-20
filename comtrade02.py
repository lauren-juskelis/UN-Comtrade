# This version incorporates a more robust version of the current year.

import requests, datetime

c = 84  # Specify country code.
now = datetime.datetime.now()
current_year = now.year

for i in range(1990, current_year):
    request = requests.get('http://comtrade.un.org/api/get/bulk/C/A/' + str(i) + '/' + str(c) + '/HS?token=mysecrettoken')
    if request.status_code != 200:
        print('File for year ' + str(i) + ' unsuccessful.')
    else:
        print('Year ' + str(i) + ' successfully accessed.')
        with open('C:/Users/ljuskelis/Desktop/UN Comtrade/' + str(c) + '.' + str(i) + '.zip', 'wb') as file:
            file.write(request.content)

print('Done.')

