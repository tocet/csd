import cv2
from picamera2 import Picamera2
import time

c_time = 0.0
p_time = 0.0

cam = Picamera2()
cam.preview_configuration.main.size = (1280,720)
cam.preview_configuration.main.format="RGB888"
cam.preview_configuration.align()
cam.configure('preview')
cam.start()

while True:
    frame = cam.capture_array()
    c_time = time.time()
    fps = int(1/(c_time - p_time))
    p_time = c_time
    cv2.putText(frame,str(fps),(15,80),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2)
    cv2.imshow("Camera preview", frame)
    if cv2.waitKey(1) == ord('x'):
        break

cv2.destroyAllWindows()
    