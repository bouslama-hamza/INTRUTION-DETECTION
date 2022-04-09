from simple_detect import SimpleDetect
import cv2 as cv
from fire_base import FireBase
import os
import glob
from datetime import datetime

# just some variables
student_number = 0
inture_number = 0

#start with downloading the new pictures
firebase = FireBase()

# use our class and load our images
simple = SimpleDetect()
simple.load_image('Desktop/raspberry pi/Detection Vase/Students/')

# start our camera 
capture = cv.VideoCapture(0)

while True :
    
    firebase.download_picture()
    n = firebase.delete_picture()
    
    if n == 1 :
        simple.load_image('Desktop/raspberry pi/Detection Vase/Students/')

    is_true , frame = capture.read()
    resized_image = cv.resize(frame, (640, 480)) 

    #start detecting faces 
    location , name = simple.knowing_faces(resized_image)

    if 'INTRUE' in name:
        # git all intrue number
        number_of_image = len(glob.glob(os.path.join('Desktop/raspberry pi/Detection Vase/Intrue/', "*.*")))
        cv.imwrite('Desktop/raspberry pi/Detection Vase/Intrue/'+str(number_of_image+1)+'.png' , resized_image)
        print("detected done")
        firebase.send_picture_new('Desktop/raspberry pi/Detection Vase/Intrue/'+str(number_of_image+1)+'.png')
        inture_number +=1
        
    if 'INTRUE' not in name:
        student_number +=1
        
    if datetime.now().strftime("%H:%M:%S") == '00:00:00':
        f = open('Desktop/raspberry pi/Detection Vase/Data File/data.txt' , 'w')
        f.write(datetime.now().strftime("%D")+","+str(student_number)+","+str(inture_number))
        f.close()
        firebase.send_data_file('Desktop/raspberry pi/Detection Vase/Data File/data.txt')
        
    key = cv.waitKey(1)
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()
