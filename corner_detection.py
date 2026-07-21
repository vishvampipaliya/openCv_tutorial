import cv2
import numpy as np

img = cv2.imread('./chess.jpg')
img = cv2.resize(img, (0, 0), fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners=corners.astype(int) 
for i in corners:
    x, y = i.ravel()
    cv2.circle(gray, (x, y), 5, (0, 255, 0), -1)
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 5)

cv2.imshow('frame', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

