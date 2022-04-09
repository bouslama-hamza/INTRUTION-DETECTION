import pyrebase
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
                'measurementId': "G-6FJXD1HXEN"
                }
        self.email    = 'Ham.bousa98@gmail.com'
        self.password = 'badBOY@2002'
        self.firebase = pyrebase.initialize_app(self.config)
        self.storage  = self.firebase.storage()
        self.auth     = self.firebase.auth()
        self.user     = self.auth.sign_in_with_email_and_password(self.email , self.password)

    def send_picture(self , image):
        self.storage.child('Students Detection/'+image.split("/")[1]).upload(image)

    def get_pictures():
        pass
