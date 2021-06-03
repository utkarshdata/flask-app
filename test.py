import requests
import json

url = 'http://192.168.1.1:5000'

data = {'Pclass': 3
      , 'Age': 2
      , 'SibSp': 1
      , 'Fare': 50}

data = json.dumps(data)

send_request = requests.post(url,data)
print(send_request)
