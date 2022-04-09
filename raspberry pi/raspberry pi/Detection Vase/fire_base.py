import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as admin_storage, credentials
import pyrebase
import os
import requests
import json
import glob
from requests import get

class FireBase():

    def __init__(self):
        self.config = {
                'apiKey': "AIzaSyBwGkE2u5JDsW0MmTmIIXA0BeZNEY-qbxQ",
                'authDomain': "first-project-db261.firebaseapp.com",
                'databaseURL': "https://first-project-db261-default-rtdb.firebaseio.com",
                'projectId': "first-project-db261",
                'storageBucket': "first-project-db261.appspot.com",
                'messagingSenderId': "134449815106",
                'appId': "1:134449815106:web:ce29163787095bc4d957db",
                'measurementId': "G-6FJXD1HXEN",
                }
        self.email    = 'Ham.bousa98@gmail.com'
        self.password = 'badBOY@2002'
        self.firebase = pyrebase.initialize_app(self.config)
        self.storage  = self.firebase.storage()
        self.auth     = self.firebase.auth()
        self.user     = self.auth.sign_in_with_email_and_password(self.email , self.password)
        self.parse    = json.loads(requests.get(self.storage.get_url(self.user['idToken'])).text)
        self.cred     = credentials.Certificate("Desktop/raspberry pi/Detection Vase/first-project-db261-firebase-adminsdk-cfpjd-e46e907571.json")
        self.admin    = firebase_admin.initialize_app(self.cred, {'storageBucket': "first-project-db261.appspot.com",})
        self.bucket   = admin_storage.bucket()

    def send_picture_new(self , image):
        self.storage.child('New Detection/'+image.split("/")[4]).upload(image)

    def send_picture_students(self , image):
        self.storage.child('Students Detection/'+image.split("/")[4]).upload(image)
        
    def send_data_file(self,image):
        self.storage.child('Data File/'+image.split("/")[4]).upload(image)
        
    def download_picture(self):
        storage  = self.firebase.storage()
        parse    = json.loads(requests.get(storage.get_url(self.user['idToken'])).text)
        for i in parse['items'] :   
            if i['name'].split("/")[0] == 'Into Accepted':
                self.storage.child(i['name']).download(filename ='Desktop/raspberry pi/Detection Vase/Students/'+i['name'].split("/")[1], token = os.path.basename('Desktop/raspberry pi/Detection Vase/Students/'+i['name'].split("/")[1]))
                print(i['name'].split("/")[1]," : done")
        
    def delete_picture(self):
        n = 0
        storage  = self.firebase.storage()
        parse    = json.loads(requests.get(storage.get_url(self.user['idToken'])).text)
        for i in parse['items'] :   
            if i['name'].split("/")[0] == 'Into Accepted':
                n = 1
                blob = self.bucket.blob('Into Accepted/'+i['name'].split("/")[1])
                blob.delete()
                print(i['name'].split("/")[1]," : deletedone")
        return n
