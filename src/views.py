from django.shortcuts import render,HttpResponse,redirect
from src.models import Blog

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        if Blog.objects.filter(email=request.POST.get('email'), password=request.POST.get('password')).exists():
            member = Blog.objects.get(email=request.POST.get('email'), password=request.POST.get('password'))
            return render(request, 'finish.html', {'member': member})
        else:
            context = {'msg': 'Invalid email or password'}
            return render(request, 'login.html', context)
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        blog=Blog(email=email,password=password)
        blog.save()
        return redirect('login')
    return render(request,'register.html')

def detail(request):
    return render(request,'detail.html')

def finish(request):
    return render(request,'finish.html')

    