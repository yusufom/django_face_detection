import cv2
import numpy as np
import os

def face_detect(image):
    p=r"/media/"
    # Get user supplied values
    image = image
    cascPath = "{base_path}/haarcascade_frontalface_default.xml".format(base_path=os.path.abspath(os.path.dirname(__file__)))
    outputfile = image[:-4]+'_detected_faces.jpg'

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imwrite(outputfile,image.astype(np.uint8))
    return outputfile