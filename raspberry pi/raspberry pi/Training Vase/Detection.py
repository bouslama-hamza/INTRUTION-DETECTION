from simple_detect import SimpleDetect
import cv2 as cv
from fire_base import FireBase

# use our class and load our images
simple = SimpleDetect()
firebase = FireBase()

number_of_image = simple.load_image('Students/')

# start our camera 
capture = cv.VideoCapture(0)

while True :
    is_true , frame = capture.read()

    #start detecting faces 
    location , name = simple.knowing_faces(frame)

    if name == 'NEW':
        cv.imwrite('Students/'+(number_of_image+1)+'.png' , frame)
        print("detection done")
        firebase.send_picture('Students/'+(number_of_image+1)+'.png')
        break

    key = cv.waitKey(1)
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()