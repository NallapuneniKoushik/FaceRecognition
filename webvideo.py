import numpy as np
import cv2
import os
from imutils import paths
import face_recognition
# import recognize_faces_video1 as re
import pickle
import encode_faces1 as ef
# import recognize_faces_video1 as re

# print("hello")
name = input("enter your Name: ")

cap = cv2.VideoCapture(0)
vid_dir= r"C:\Users\MyPC\Downloads\face-recognition-opencv\face-recognition-opencv\videos"
dataset_dir = r"C:\Users\MyPC\Downloads\face-recognition-opencv\face-recognition-opencv\dataset"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(f"{vid_dir}/{name}.mp4",fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

os.mkdir(f"{dataset_dir}/{name}")

vidcap = cv2.VideoCapture(f'{vid_dir}/{name}.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(f"{dataset_dir}/{name}/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

print("Conversion done!")
# ef.encode( dataset_dir, "hog" , "encodings.pickle")

print("Encoding done")
print("Running detection")

re.recog("hog", "encodings.py")