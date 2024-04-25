from django.shortcuts import render, redirect
from app.models import users, roles, Servicios
from app.forms import *
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
import base64
from django.contrib import messages
# Funcion para analizar si el string recibido esta en base64
# y parsear si contiene las palabras 'alert' o 'script'
# en caso afirmativo, se arroja error, caso contrario
# se retorna el valor ingresado
def sanitizar_input(input_data):
    try:
        decoded_data = base64.b64decode(input_data).decode('utf-8')
        for keyword in ['script', 'alert', 'x28', 'x29']:
            if keyword in decoded_data.lower():
                raise ValueError("Error en el input de datos: contiene palabras clave no deseadas.")
        return decoded_data
    except (base64.binascii.Error, UnicodeDecodeError):
        return input_data

# Create your views here.
def index(request):
        return render(request, 'index.html')

def quote(request):
        return render (request, 'quote.html')

def service(request):
    return render(request, 'Servicios.html')

def about(request):
    return render(request, 'about.html')

def choose(request):
    return render(request, 'choose.html')

def team(request):
    return render(request, 'team.html')

def editservices(request):
    # Verificar si es admin
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                servicios = Servicios.objects.all()
                return render(request, 'EditServices.html', {'services': servicios})
            except Exception as e:
                print(e)
                return HttpResponse('<h1>Servicios no encontrados</h1>') 
        elif request.method == 'POST':
            selected_service = request.POST.get('selected_service')
            return redirect('Edit Services', pk=selected_service)
        else:
            return redirect('index')
    else:
        return redirect('index')

def edit_service_details(request, pk):
    # Verificar si el usuario está autenticado y es un administrador
    # Verificar si el usuario está autenticado y es un administrador
    if request.user.is_authenticated:
        servicio = get_object_or_404(Servicios, service_id=pk)
        # if request.method == 'GET':
        #     form = EditServicesForm(instance=servicio)
        if request.method == 'POST':
            form = EditServicesForm(request.POST, instance=servicio)
            if form.is_valid():
                try:
                    datos = form.cleaned_data
                    service_price = datos["service_price"]
                    service_qty = datos["service_qty"]
                    service_name_clean = sanitizar_input(datos["service_name"])
                    service_description_clean = sanitizar_input(datos["service_description"])
                    servicio.service_name = service_name_clean
                    servicio.service_description = service_description_clean
                    servicio.service_price = service_price
                    servicio.service_qty = service_qty
                    servicio.save()
                    return redirect('List Services')
                except ValueError as e:
                    messages.error(request, "Datos inválidos: " + str(e))
            # Si el formulario no es válido, se renderiza nuevamente la página con el formulario y los errores
        else:
            form = EditServicesForm(instance=servicio)
            # Si el método de solicitud no es POST, se crea un formulario vacío con los datos del servicio
        return render(request, 'EditServiceDetails.html', {'form': form})
    else:
        return redirect('index')

# def input_is_clean(input_data):
#     try:
#         decoded_data = base64.b64decode(input_data).decode('utf-8')
#         for keyword in ['script', 'alert']:
#             if keyword in decoded_data.lower():
#                 return False  # Retorna False si se encuentran palabras clave no deseadas
#         return True  # Retorna True si los datos están limpios
#     except (base64.binascii.Error, UnicodeDecodeError) as e:
#         raise ValueError("Error en la decodificación de datos: " + str(e))  


# def edit_service_details(request, pk):
#     if request.user.is_authenticated:
#         servicio = get_object_or_404(services, service_id=pk)
#         if request.method == 'GET':
#             form = EditServicesForm(instance=servicio)
#         elif request.method == 'POST':
#             form = EditServicesForm(request.POST, instance=servicio)
#             if form.is_valid():
#                 datos = form.cleaned_data
#                 try:
#                     if input_is_clean(datos["service_name"]) and input_is_clean(datos["service_description"]):
#                         form.save()
#                         return redirect('List Services')
#                     else:
#                         # Reasignar el formulario para que se vuelva a mostrar con los datos originales
#                         form = EditServicesForm(instance=servicio)
#                         messages.error(request, "Datos inválidos: contiene palabras clave no deseadas.")
#                 except ValueError as e:
#                     # Manejar la excepción ValueError que podría ser elevada por input_is_clean
#                     messages.error(request, "Error en la decodificación de datos: " + str(e))
#             # Si el formulario no es válido, se renderiza nuevamente la página con el formulario y los errores
#         else:
#             # Reasignar el formulario para que se vuelva a mostrar con los datos originales
#             form = EditServicesForm(instance=servicio)
#         return render(request, 'EditServiceDetails.html', {'form': form})
#     else:
#         return redirect('index')



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')

def invoice_generator(request):
    if request.user.is_authenticated:
        servicios = Servicios.objects.all()
        return render(request, 'InvoiceGenerator.html', {'Servicios': servicios})
    else:
        return redirect('index')
    
def test(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            datos_formulario = form.cleaned_data
            # Buscar el registro en la base de datos
            objeto, creado = Clientes.objects.get_or_create(datos_formulario['email'], datos_formulario)  # Utiliza los datos del formulario como valores predeterminados
            
            # Si el objeto ya existía, actualiza los campos
            if not creado:
                for campo, valor in datos_formulario.items():
                    setattr(objeto, campo, valor)
                objeto.save()
            return redirect('mi_urta')  # Redirigir a donde desees después de procesar el formulario
    else:
        form = ClientesForm()
    return render(request, 'mi_template.html', {'form': form})