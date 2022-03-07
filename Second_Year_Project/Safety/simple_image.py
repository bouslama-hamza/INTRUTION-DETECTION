import pyrebase
import requests
import json
from io import BytesIO
from PIL import Image
from requests import get

class SimpleImage():
    
    def __init__(self):
        self.config = {
                    'apiKey': "AIzaSyBwGkE2u5JDsW0MmTmIIXA0BeZNEY-qbxQ",
                    'authDomain': "first-project-db261.firebaseapp.com",
                    'databaseURL': "https://first-project-db261-default-rtdb.firebaseio.com",
                    'projectId': "first-project-db261",
                    'storageBucket': "first-project-db261.appspot.com",
                    'messagingSenderId': "134449815106",
                    'appId': "1:134449815106:web:ce29163787095bc4d957db",
                    'measurementId': "G-6FJXD1HXEN"
                }
        self.firebase = pyrebase.initialize_app(self.config)
        self.storage  = self.firebase.storage()
        self.auth     = self.firebase.auth()
        self.email    = 'Ham.bousa98@gmail.com'
        self.password = 'badBOY@2002'
        self.user     = self.auth.sign_in_with_email_and_password(self.email , self.password)
        self.parse    = json.loads(requests.get(self.storage.get_url(self.user['idToken'])).text)
        
    def upload_image(self , path , target):
        self.storage.child(path).upload(target)

    def get_image(self , order):
        lest = []
        for i in self.parse['items'] :
            if i['name'].split("/")[0] == order[0]+" "+order[1]:
                test_url = 'https://firebasestorage.googleapis.com/v0/b/first-project-db261.appspot.com/o/'+order[0]+'%20'+order[1]+'%2F'+i['name'].split("/")[1]+'?alt=media'
                image_raw = get(test_url)
                image = Image.open(BytesIO(image_raw.content))
                width , height = image.size
                lest.append({'name' : i['name'].split("/")[1] , 'url' : test_url , 'size' : [width , height]})
        return lest