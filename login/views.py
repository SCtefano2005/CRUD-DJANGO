from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # da la plantilla del formulario B)
from django.contrib.auth.models import User # ayuda para guardar los datos osea es un modelo predeterminado de laravel
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
