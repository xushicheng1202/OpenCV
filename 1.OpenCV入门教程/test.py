import cv2 as cv

face_cascade = cv.CascadeClassifier(
    'C:\ProgramData\Anaconda3\envs\OpenCV\Library\etc\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\ProgramData\Anaconda3\envs\OpenCV\Library\etc\haarcascades\haarcascade_eye.xml')

img = cv.imread('image/lenacolor.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

cv.imshow('Face_Detect', img)
cv.waitKey()
cv.destroyAllWindows()
