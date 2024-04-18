from django.shortcuts import render, redirect
from app.models import users, roles, services
from app.forms import EditServicesForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
        return render(request, 'index.html')

def quote(request):
        return render (request, 'quote.html')

def service(request):
    return render(request, 'services.html')

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
                servicios = services.objects.all()
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
    if request.user.is_authenticated:
        servicio = get_object_or_404(services, service_id=pk)
        if request.method == 'GET':
            form = EditServicesForm(instance=servicio)
        elif request.method == 'POST':
            form = EditServicesForm(request.POST, instance=servicio)
            if form.is_valid():
                form.save()
                return redirect('index')
            # Si el formulario no es válido, se renderiza nuevamente la página con el formulario y los errores
        return render(request, 'EditServiceDetails.html', {'form': form})
    else:
        return redirect('index')
    
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