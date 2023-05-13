import cv2

img = cv2.imread('jjj/s_1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier('face.xml')

results = face.detectMultiScale(gray, scaleFactor=2, minNeighbors=3)
for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (10, 10, 400), thickness=2)

cv2.imshow("Result", img)
cv2.waitKey(0)