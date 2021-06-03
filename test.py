import requests
import json

heroku_url = 'https://gradwise-front-end.herokuapp.com/'

data = {'School_Stanford': 1,
'School_Wharton': 0,
'School_Chicago Booth': 0,
'School_Kellogg': 0,
'School_Harvard': 0,
'School_MIT Sloan': 0,
'School_Columbia': 0,
'School_UC Berkeley': 0,
'School_Yale': 0,
'School_Dartmouth': 0,
'School_NYU Stern': 0,
'School_Duke Fuqua': 0,
'School_Michigan Ross': 0,
'School_Darden': 0,
       
 'Year_2017': 1,
'Year_2018': 0,
'Year_2019': 0,
'Year_2020': 0,
'Year_2021': 0,
'Year_2022': 0 }

data = json.dumps(data)

send_request = requests.post(url,data)
print(send_request)
print(send_request.json())

