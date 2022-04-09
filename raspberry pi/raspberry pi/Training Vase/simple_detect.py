import face_recognition
import cv2 as cv
import os
import glob
import numpy as np

# create our class

class SimpleDetect:
    
    def __init__(self):
        self.face_numpy = []
        self.face_names = []

        # change demonsion of image
        self.size = 0.3
    
    # methode to load our images
    def load_image(self , path):
        path = glob.glob(os.path.join(path, "*.*"))
        print("Number of Image founded : ", len(path))

        # save the name and image
        for i in path:
            img = cv.imread(i)
            rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            name = os.path.basename(i)
            (filename, ext) = os.path.splitext(name)
            
            
            # part of encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]
            self.face_numpy.append(img_encoding)
            self.face_names.append(filename)

        print("Its working..........")
        return len(path)

    # we gonna use this methode to detect all knowing faces
    def knowing_faces(self , frame):
        
        small_img = cv.resize(frame, (0, 0), fx = self.size, fy = self.size)

        rgb_small_frame = cv.cvtColor(small_img, cv.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # time to match between pictures
        face_names = []
        for i in face_encodings:
            same = face_recognition.compare_faces(self.face_numpy, i)
            name = 'NEW'

            distances = face_recognition.face_distance(self.face_numpy, i)
            min_distance = np.argmin(distances)
            
            if same[min_distance] == True:
                name = self.face_names[min_distance]

            face_names.append(name)

        face_locations = np.array(face_locations)
        face_locations = face_locations / self.size

        return face_locations.astype(int) , face_names
    
    # we gonna create a method so we can collect our data base