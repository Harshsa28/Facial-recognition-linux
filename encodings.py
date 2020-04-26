import face_recognition
import cv2
import numpy as np
import pickle
import os

encodings = []
names = []

train_dir = os.listdir('input_dir')
for person in train_dir:
    face = face_recognition.load_image_file('input_dir' + person)
    face_bounding_boxes = face_recognition.face_locations(face)
    if len(face_bounding_boxes) == 1:
        face_enc = face_recognition.face_encodings(face)[0]
        encodings.append(face_enc)
        names.append('your name')
    else:
        print(person + "was skipped and can't be used for training")

#print(encodings, file=open('encodings.txt', 'w'))
#print(names, file=open('names.txt' , 'w'))

#print("type of encodings is :" , type(encodings))
#print("type of names is :" , type(names))

with open('encodings.pkl', 'wb') as output:
    pickle.dump(encodings, output, pickle.HIGHEST_PROTOCOL)
with open('names.pkl' , 'wb') as output:
    pickle.dump(names, output, pickle.HIGHEST_PROTOCOL)
