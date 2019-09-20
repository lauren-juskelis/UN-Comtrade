import requests

c = 84  # Specify country code.

for i in range(1990, 2018):
    request = requests.get('http://comtrade.un.org/api/get/bulk/C/A/' + str(i) + '/' + str(c) + '/HS?token=mysecrettoken')
    if request.status_code != 200:
        print('File for year ' + str(i) + ' unsuccessful.')
    else:
        print('Year ' + str(i) + ' successfully accessed.')
        with open('C:/Users/ljuskelis/Desktop/UN Comtrade/' + str(c) + '.' + str(i) + '.zip', 'wb') as file:
            file.write(request.content)

print('Done.')

