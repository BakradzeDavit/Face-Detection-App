import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('RBJ.jpg')

"""
e
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



for (x, y, w, h) in face_coordinates:
cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 5)

cv2.imshow('Clever programmer face detector', img)
cv2.waitKey()   
"""
webcam = cv2.VideoCapture(0)
while True:
    succesful_frame_read, frame = webcam.read()
    frame = cv2.flip(frame, 1) 
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256) ), 5)


    cv2.imshow('Clever programmer face detector', frame)
    key = cv2.waitKey(1)   

    if key ==81 or key == 113:
        break

webcam.release()       
