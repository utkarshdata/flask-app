import requests
import json

heroku_url = 'https://gradwise-front-end.herokuapp.com/'

data = {'Pclass': 3
      , 'Age': 2
      , 'SibSp': 1
      , 'Fare': 50}

data = json.dumps(data)

send_request = requests.post(url,data)
print(send_request)
