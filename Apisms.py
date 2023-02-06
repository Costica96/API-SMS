import json
import requests 
from twilio.rest import Client 

API_KEY = "ee19d79f2b5a4983a0f133411220312"

api_uri = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Bucharest")

# response =api_uri.json()
# print(response)

city_response = api_uri.json()["location"]["name"]
date_response = api_uri.json()["location"]["localtime"].split(" ")[0]
time_response = api_uri.json()["location"]["localtime"].split(" ")[1]
temp_response = api_uri.json()["current"]["temp_c"]
weather_response = api_uri.json()["current"]["condition"]["text"]
humidity_response = api_uri.json()["current"]["humidity"]

weather_message = (f"In {city_response} today, {date_response} at {time_response} are {temp_response} Celsius degrees. Day is {weather_response}, with {humidity_response} % humidity. \nIt's a perfect day to stay home and learn Python!")
print(weather_message)

account_sid = 'AC3f51b25dfee924b2b2ed4f109426484f'
auth_token = 'd2bb858237f7a9ed328964ecddf5a129'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=weather_message,
                     from_='+18058746587',
                     to='+40775141594'
                 )

print(message.sid)