from django.shortcuts import render
from Safety.simple_image import SimpleImage
from .forms import UserUpdateForm , UserLoginForm
from django.contrib.auth.decorators import login_required
from Safety.send_email import send_email
from django.contrib.auth.models import User
from Safety.make_plot_data import make_data , make_pie , make_plot
from Safety.load_data import load_data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as admin_storage, credentials
import os

@login_required
def app(request):
    global data_set
    global bucket
    try:
        cred     = credentials.Certificate('Safety/static/JS/first-project-db261-firebase-adminsdk-cfpjd-9e7480d0c5.json')
        admin    = firebase_admin.initialize_app(cred , {'storageBucket': "first-project-db261.appspot.com",})
        bucket   = admin_storage.bucket()
        simple   = SimpleImage()
        simple.get_data_file(bucket)
        load_data()
    except:
        print("no Data")
    make_pie()
    make_plot()
    data_set = make_data()
    return render(request , 'app.html' , {'title' : 'DashBoard' , 'data' : data_set})

@login_required
def compenents(request):
    simple = SimpleImage()
    data = simple.get_image(['Students','Detection'])
    if request.method == 'POST':
        simple.upload_image('Into Accepted' , 'Safety/static/NewStudent/'+request.POST.get('file'))
        simple.upload_image('Students Detection'  , 'Safety/static/NewStudent/'+request.POST.get('file'))
        message = "File Has been added Succefully , Wait For Rassbery To Be Accepted"
        return render(request , 'compenents.html' , {'image' : data , 'title' : 'Compenents' , 'message' : message})
    return render(request , 'compenents.html' , {'image' : data , 'title' : 'Compenents'})

@login_required
def intrue(request):
    simple = SimpleImage()
    data = simple.get_image(['Intrue','Detection'])
    return render(request , 'intrue.html' , {'image' : data , 'title' : 'Intrue Detection'})

@login_required
def new_intrue(request):
    simple = SimpleImage()
    data = simple.get_image(['New','Detection'])
    if request.method == 'POST':
        if request.POST['send'] == 'Students':
            image = request.POST['name']
            simple = SimpleImage()
            simple.download_image(image , bucket)
            simple.upload_image('Into Accepted' , 'Safety/static/TRANFER/'+image)
            simple.upload_image('Students Detection'  , 'Safety/static/TRANFER/'+image)
            os.remove('Safety/static/TRANFER/'+image)
            message = 'Students Has beein Classified Succesfully'
            return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection' , 'message':message})
        elif request.POST['send'] == 'Intrues':
            image = request.POST['name']
            simple = SimpleImage()
            simple.download_image(image , bucket)
            simple.upload_image('Intrue Detection'  , 'Safety/static/TRANFER/'+image)
            os.remove('Safety/static/TRANFER/'+image)
            message = 'Students Has beein Classified Succesfully'
            return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection' , 'message':message})
    return render(request , 'new_intrue.html' , {'image' : data , 'title' : 'New Intrue Detection'})

@login_required
def manage_account(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance = request.user)
        if update_form.is_valid():
            request.user.set_password(update_form.cleaned_data.get('password2'))
            update_form.save()
            message = 'Setting has been Updating Successfully'
            return render(request , 'manage_account.html' , {'update_form':update_form , 'message':message , 'title' : 'Manage Account'})
        else:
            error = 'Invalid Information Please Try Again'
            return render(request , 'manage_account.html' , {'update_form':update_form , 'error':error , 'title' : 'Manage Account'})
    else:
        update_form = UserUpdateForm(instance = request.user)
    return render(request, 'manage_account.html' , {'title' : 'Manage Account' , 'update_form':update_form} )
    
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