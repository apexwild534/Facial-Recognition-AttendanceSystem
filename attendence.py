import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# fetching images
path = 'ImagesAttendence'
images = []  # to store images
classNames = []  # to store names
myList = os.listdir(path)  # returns list of all files/directories in path
print(f"Found files: {myList}")

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])  # store part before extension
    else:
        print(f"Error reading image {cl}")
print(f"Class Names: {classNames}")


# Find encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if len(encodes) > 0:
            encodeList.append(encodes[0])  # store first detected face encoding
        else:
            print("No face found in image.")
    return encodeList


# Mark attendance
def markAttendance(name, regisNo):
    with open('attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')  #format the time string
            f.writelines(f'\n{name},{regisNo},{dtString}')
            print(f"Attendance marked for {name}")


#find encodings for known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

#video capture
cap = cv2.VideoCapture(0)
fps_start_time = datetime.now()

while True:
    success, img = cap.read()  #capture frame-by-frame
    if not success:
        print("Failed to capture video frame.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Downsize for faster processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    #find matches
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)  #get the closest match
        if matches[matchIndex]:
            stuDetail = classNames[matchIndex].split('_')
            name = stuDetail[0].upper()
            regisNo = stuDetail[1] if len(stuDetail) > 1 else 'Registration Number Not Found'

            #display the name and rectangle around the face
            y1, x2, y2, x1 = [v * 4 for v in faceLoc]  #rescale the locations
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name, regisNo)
        else:
            #mark as intruder if no match found
            y1, x2, y2, x1 = [v * 4 for v in faceLoc]
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, 'Intruder', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    #display the FPS on the frame
    fps_end_time = datetime.now()
    time_diff = fps_end_time - fps_start_time
    fps = 1 / time_diff.total_seconds()
    fps_start_time = fps_end_time
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #show webcam feed
    cv2.imshow('webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
