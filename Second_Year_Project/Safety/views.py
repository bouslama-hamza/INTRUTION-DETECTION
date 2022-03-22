from django.shortcuts import render
from Safety.simple_image import SimpleImage
from .forms import UserUpdateForm , UserLoginForm
from django.contrib.auth.decorators import login_required
from Safety.send_email import send_email
from django.contrib.auth.models import User
from Safety.make_plot_data import make_data , make_pie , make_plot
from Safety.load_data import load_data
import os

# use our fire base class
global simple
simple = SimpleImage()
global data_set
global isintrue

@login_required
def app(request):
    # in case there is new intrue 
    isintrue = False
    data = simple.get_image(['New','Detection'])
    if data:
        isintrue = True
    try:
        simple.get_data_file()
        load_data()
    except:
        print("no Data")
    pie = make_pie()
    test = make_plot()
    data_set = make_data()
    return render(request , 'app.html' , {'title' : 'DashBoard' , 'data' : data_set , 'test' : test, 'pie' : pie,'isintrue' : isintrue})

@login_required
def compenents(request):
    # in case there is new intrue 
    isintrue = False
    data = simple.get_image(['New','Detection'])
    if data:
        isintrue = True
    try:
        data = simple.get_image(['Students','Detection'])
        if request.method == 'POST':
            simple.upload_image('Into Accepted' , 'Safety/static/NewStudent/'+request.POST.get('file'))
            simple.upload_image('Students Detection'  , 'Safety/static/NewStudent/'+request.POST.get('file'))
            message = "File Has been added Succefully , Wait For Rassbery To Be Accepted"
            return render(request , 'compenents.html' , {'image' : data , 'title' : 'Compenents' , 'message' : message , 'isintrue' : isintrue})
        return render(request , 'compenents.html' , {'image' : data , 'title' : 'Compenents' , 'isintrue' : isintrue})
    except:
        data_set = make_data()
        error = 'Please Check Your Connection And Try Again'
        return render(request , 'app.html' , {'title' : 'DashBoard' , 'data' : data_set , 'error' : error , 'isintrue' : isintrue})

@login_required
def intrue(request):
    # in case there is new intrue 
    isintrue = False
    data = simple.get_image(['New','Detection'])
    if data:
        isintrue = True
    try:
        data = simple.get_image(['Intrue','Detection'])
        return render(request , 'intrue.html' , {'image' : data , 'title' : 'Intrue Detection' , 'isintrue' : isintrue})
    except:
        data_set = make_data()
        error = 'Please Check Your Connection And Try Again'
        return render(request , 'app.html' , {'title' : 'DashBoard' , 'data' : data_set , 'error' : error , 'isintrue' : isintrue})   

@login_required
def new_intrue(request):
    isintrue = False
    try :
        data = simple.get_image(['New','Detection'])
        if data:
            isintrue = True
        if request.method == 'POST':
            if request.POST['send'] == 'Students':
                image = request.POST['name']
                simple.download_image(image)
                simple.upload_image('Into Accepted' , 'Safety/static/TRANFER/'+image)
                simple.upload_image('Students Detection'  , 'Safety/static/TRANFER/'+image)
                os.remove('Safety/static/TRANFER/'+image)
                message = 'Students Has beein Classified Succesfully'
                data = simple.get_image(['New','Detection'])
                return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection' , 'message':message , 'isintrue' : isintrue})
            elif request.POST['send'] == 'Intrues':
                image = request.POST['name']
                simple.download_image(image)
                simple.upload_image('Intrue Detection'  , 'Safety/static/TRANFER/'+image)
                os.remove('Safety/static/TRANFER/'+image)
                message = 'Students Has beein Classified Succesfully'
                data = simple.get_image(['New','Detection'])
                return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection' , 'message':message , 'isintrue' : isintrue})
        return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection' , 'isintrue' : isintrue})
    except :
        data_set = make_data()
        error = 'Please Check Your Connection And Try Again'
        return render(request , 'app.html' , {'title' : 'DashBoard' , 'data' : data_set , 'error' : error , 'isintrue' : isintrue})   

@login_required
def manage_account(request):
    # in case there is new intrue 
    isintrue = False
    data = simple.get_image(['New','Detection'])
    if data:
        isintrue = True
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance = request.user)
        if update_form.is_valid():
            request.user.set_password(update_form.cleaned_data.get('password2'))
            update_form.save()
            message = 'Setting has been Updating Successfully'
            return render(request , 'manage_account.html' , {'update_form':update_form , 'message':message , 'title' : 'Manage Account' , 'isintrue' : isintrue})
        else:
            error = 'Invalid Information Please Try Again'
            return render(request , 'manage_account.html' , {'update_form':update_form , 'error':error , 'title' : 'Manage Account' ,  'isintrue' : isintrue})
    else:
        update_form = UserUpdateForm(instance = request.user)
    return render(request, 'manage_account.html' , {'title' : 'Manage Account' , 'update_form':update_form , 'isintrue' : isintrue} )
    
def reset_password(request):
    global change_number
    global user
    if request.method == 'POST':
        email = request.POST.get('change_me')
        try :
            user = User.objects.get(email = email)
            change_number = send_email()
            return render(request ,'password_reset_confirm.html' , {'title' : 'Change Password'})
        except:
            message = 'This User Dont Have An Account , please chaque your information'
            return render(request , 'password_rest.html' , {'message':message , 'title' : 'Reset Password'})
    return render(request , 'password_rest.html' , {'title' : 'Reset Password'})

def confirm_reset(request):
    if request.method == 'POST':
        if change_number != int(request.POST.get('change_password')):
            message = 'Error !,wrong Number please chaque and try Again'
            return render(request , 'password_rest_confirm.html' , {'message' : message , 'title' : 'Change Password'})
        elif request.POST.get('password_change') != request.POST.get('conf_password_change'):
            message = 'Error!, Password and Confirm password are not the same'
            return render(request , 'password_rest_confirm.html' , {'message' : message , 'title' : 'Change Password'})
        else:
            user.set_password(request.POST.get('conf_password_change'))
            user.save()
            form = UserLoginForm()
            messages = 'Your password has been change Successfully'
            return render(request , 'password_rest.html' , {'form' : form , 'messages' : messages , 'title' : 'Reset Password'})
    return render(request , 'password_reset_confirm.html' , {'title' : 'Change Password'})