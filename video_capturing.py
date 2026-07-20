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

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

