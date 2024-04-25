import cv2
import time

c_time = 0.0
p_time = 0.0

img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
img.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _, frame = img.read()
    cv2_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    c_time = time.time()
    fps = int(1/(c_time - p_time))
    p_time = c_time
    cv2.putText(cv2_frame,str(fps),(15,80),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2)
    cv2.imshow("Camera",cv2_frame)
    if cv2.waitKey(1) == ord('x'):
        break

cv2.destroyAllWindows()
    