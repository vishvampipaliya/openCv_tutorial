import cv2
import numpy as np

img = cv2.imread('./images.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#basic image operations
print(img)
print(img.shape)
print(img.dtype)

# image color space conversion

image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(image)
cv2.imshow('image', image)

image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(image)
cv2.imshow('image', image)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.imshow('gray', gray)

# image numberical operations

print(np.max(img))
print(np.min(img))
print(np.mean(img))
print(np.std(img))

# image filtering

blur = cv2.GaussianBlur(gray, (5, 5), 0)
# print(blur)
cv2.imshow('blur', blur)

thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]
print(thresh) 
cv2.imshow('thresh', thresh)

# image resizing and rotation

image = cv2.resize(img, (0, 0), fx=2, fy=2)
cv2.imshow('image', image)

image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
image = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('image', image)

# image edge detection
image = cv2.Canny(img, 100, 200)
cv2.imshow('image', image)


cv2.waitKey(0)
cv2.destroyAllWindows()