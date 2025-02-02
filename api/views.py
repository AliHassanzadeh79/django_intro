from django.shortcuts import render
from django.http import HttpResponse
import string , random , requests
# Create your views here.

def generate_password (request):
    length = 12
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(password)
# Route for random-number and Show description
def random_number (request):
    num = random.randint(1,1000)
    response = requests.get(f"http://numbersapi.com/{num}")
    return HttpResponse(f"random number : {num}<br>{response.text}")
# Route for Kerman's Weather
def weather (request):
    response = requests.get("https://wttr.in/kerman?format=j1")
    weather_data = response.json()
    current_condition = weather_data['current_condition'][0]
    temp_C = current_condition['temp_C']
    windspeedKmph = current_condition['windspeedKmph']
    humidity = current_condition['humidity']
    return HttpResponse( f'دمای فعلی: {temp_C} درجه سانتی‌گراد، سرعت باد: {windspeedKmph} کیلومتر بر ساعت، درصد رطوبت: {humidity} درصد')
