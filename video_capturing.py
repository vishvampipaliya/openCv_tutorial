import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    image = np.zeros(frame.shape, dtype=np.uint8)
    smaaler_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaaler_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaaler_frame
    image[:height//2, width//2:] = cv2.rotate(smaaler_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaaler_frame

    # cv2.imshow('frame', image)


    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)

    img=cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)

    img=cv2.rectangle(img, (width//4, height//4), (width*3//4, height*3//4), (0, 0, 255), 5)
    img=cv2.circle(img, (width//2, height//2), 100, (0, 0, 255), 5)
    img=cv2.putText(img, 'OpenCV', (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

    cv2.imshow('line', img)



    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

