from django.shortcuts import redirect, render
from Safety.simple_image import SimpleImage

def home(request):
    if request.method == 'POST':
        return redirect('safety-app')
    return render(request , 'login.html')

def app(request):
    return render(request , 'dashboard.html')

def compenents(request):
    simple = SimpleImage()
    data = simple.get_image(['Students','Detection'])
    return render(request , 'compenents.html' , {'image' : data})

def intrue(request):
    simple = SimpleImage()
    data = simple.get_image(['Intrue','Detection'])
    return render(request , 'intrue.html' , {'image' : data})
    
def new_intrue(request):
    simple = SimpleImage()
    data = simple.get_image(['New','Detection'])
    return render(request , 'new_intrue.html' , {'image' : data})

    
