from django.shortcuts import render
from django.http import HttpResponse
import string , random
# Create your views here.
def generate_password (request):
    length = 12
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return HttpResponse(password)
