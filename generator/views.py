from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    thepassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?><]['))

    if request.GET.get('numbers'):
        characters.extend(list('012345678910'))


    length  = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def information(request):
    return render(request, 'generator/information.html')
