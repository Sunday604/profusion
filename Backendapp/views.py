from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Datebase
# Create your views here.
# @login_required(login_url='/accounts/login')
def home(request):
     if request.method =='POST':
        names = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data =Datebase(name=names, email=email, phone=phone, message=message)
        data.save()
     return render(request, 'index.html')


@login_required(login_url='/accounts/login')
def contact(request):
     if request.method =='POST':
        names = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data =Datebase(name=names, email=email, phone=phone, message=message)
        data.save()
     return render(request, 'contact.html')


def database(request):
    data = Datebase.objects.all()
    context ={
        'data': data
    }
    return render(request, 'database.html', context)




def update(request, id):
    updateInfo = Datebase.objects.get(id=id)
    
    if request.method == 'POST':
        updateInfo.name = request.POST.get('name')
        updateInfo.email = request.POST.get('email')
        updateInfo.phone = request.POST.get('phone')
        updateInfo.message = request.POST.get('message')
        updateInfo.save()
        return redirect('database')
    context = {
        'updateInfo': updateInfo
    }
    return render(request, 'update.html', context)


def delete(request, id):
    item = Datebase.objects.get(id=id)
    item.delete()
    return redirect('database')





def about(request):
    return render(request, "about.html")

def client(request):
    return render(request, "client.html")

def service(request):
    return render(request, "services.html")
