from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # da la plantillas del formulario B)
from django.contrib.auth.models import User # ayuda para guardar los datos osea es un modelo predeterminado de laravel
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse 



def registrar(request):
    if request.method == 'GET': # si la solicitud es GET muestra el formulario 
        return render(request, 'signup.html', {
            'form': UserCreationForm # aca carga la plantilla del formulario de registro de django forms 
        })
    else: 
        if request.POST['password1'] == request.POST['password2']: # aca compara las contraseñas para que sean iguales
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'] # aca captura el username y el password
                ) 
                user.save() # aca lo guarda en la bd
                login(request, user)
                #return redirect('parametro o url')
            except: # retorna la plantilla de formulario con el error de el usuario esta registrado
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya esta registrado'
                })
        return render(request, 'signup.html', { # retorna la plantilla de formulario con el error de contraseñas no iguales 
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def home(request):
    return render(request, 'index.html')

def salir(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'logint' : AuthenticationForm()
        })
    else: 
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'logint' : AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })