import requests

request = requests.get('http://comtrade.un.org/api/get/bulk/C/A/2018/84/HS?token=mysecrettoken')
print(request.status_code)

with open('C:/Users/ljuskelis/Desktop/UN Comtrade/84.2018.zip', 'wb') as file:
    file.write(request.content)

print('Done.')
