import cv2,time
from playsound import playsound

video = cv2.VideoCapture(0)

first_Frame = None

while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray =cv2.GaussianBlur(gray,(21,21),0)
    if first_Frame is None:
        first_Frame = gray
        continue
    delta_frame = cv2.absdiff(first_Frame,gray)
    threshold_frame = cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame,None,iterations=2)

    (cntr,_) = cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    count =1 
    for contour in cntr:

        if cv2.contourArea(contour)<500:
            continue
        
        (x,y,w,h) = cv2.boundingRect(contour)
        print("yamede kuramasai")
        first_Frame = gray
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        count+=1
        print(count)
        if count%4==0:
            playsound('/home/harsh/Documents/prank-pi/13.mp3')

    cv2.imshow("cvfdsfd",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()