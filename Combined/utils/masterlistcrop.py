import cv2
import time
from PIL import Image

def extended_Coordinates(frame,face_coordinates):
    extended_Coordinates=[]
    img = Image.fromarray(frame)
    width, height = img.size
    for i in face_coordinates:
        w=i[2]-i[0]
        h=i[3]-i[1]       
        l = []      
        if(i[0] - w/2 < 0):
            l.append(0)
        else:
            l.append(i[0] - w/2)
        if(i[1] - h/2 < 0):
            l.append(0)
        else:
            l.append(i[1] - h/2)
        if(i[0] + 3*w/2 > width - 1):
            l.append(width - 1)
        else:
            l.append(i[0] + 3*w/2)
        if(i[1] + 3*h/2 > height - 1):
            l.append(height-1)
        else:
            l.append(i[1] + 3*h/2)
        extended_Coordinates.append(l)
    return extended_Coordinates
def cropped_image(frame,extended_Coordinates):
    k=0
    for i in extended_Coordinates:
        face_roi = frame[int(i[1]):int(i[3]), int(i[0]):int(i[2])]
        cv2.imshow(f'Face{k+1}',face_roi)
        k+=1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def face_coordiantes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    frame_list.append(frame)
    for (x, y, w, h) in faces:
        # Draw rectangles around faces
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Save face coordinates in the list
        face_coordinates.append([x, y, x+w, y+h])
    return face_coordiantes
# Load the Haarcascades classifiers for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Open video capture for webcam (usually index 0)
cap = cv2.VideoCapture(0)
#sleep 15 secs for students to settle to get initial frame
time.sleep(2)
face_coordinates = []
wid_height=[]
frame_list=[]
no_of_faces_in_frame=[]
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    face_coordiantes(frame)
    cv2.imshow('Live Video', frame)
    if(len(frame_list)==1):
        break
#print("Frame",frame_list)
print("Face Coordinates:", face_coordinates)
ec=list(extended_Coordinates(frame_list[0],face_coordinates))
print("extended_coordinates:",ec)
cropped_image(frame_list[0],ec)

