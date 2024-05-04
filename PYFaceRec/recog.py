import face_recognition
import cv2


# ! KNOWN FACES AND ENCODINGS ! #

known_face_encodings = []
known_face_names = []


# ! LOAD KNOWN FACES AND NAMES ! #

known_person1_image = face_recognition.load_image_file("countdooku.jfif")
known_person2_image = face_recognition.load_image_file("godfather.jfif")
known_person3_image = face_recognition.load_image_file("foto.jpg")

known_person1_encodings = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encodings = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encodings = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encodings)
known_face_encodings.append(known_person2_encodings)
known_face_encodings.append(known_person3_encodings)


known_face_names.append("Count Dooku")
known_face_names.append("GodFather")
known_face_names.append("Ahmet Utku Pelen")


# ! WEBCAM PART ! #

video_capture = cv2.VideoCapture(0)

while True:
    # capture frames #
    ret,frame = video_capture.read()
    
    # find all locations in current frame #
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame,face_locations)
    
    # loop each face found in frame #
    for (top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):
        #  check if face mathces any known faces #
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        name = "Unknown"
        
        if  True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
        #  draw box around face and label face with a name #
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame,name, (left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
        
    # DISPLAY RESULTING FRAME #
    cv2.imshow("Video",frame)
    
    # BREAK THE LOOP WHEN PRESSING Q #
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
#  RELEASE WEB CAM AND CLOSE OPENCV WINDOWS #
video_capture.release()
cv2.destroyAllWindows()