import requests
response = requests.get('https://stackoverflow.com/questions/16778435/python-check-if-website-exists')
if response.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist') 