from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Criação de end-points (location on the web server)

def main(request): #envia o request e recebe a response do web server pode ser json, html...
    return HttpResponse('Hello')

#qual o caminho para essa response? -> urls.py