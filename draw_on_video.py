import cv2
import datetime
carVid=cv2.VideoCapture("D:\\openCV python\\muuuu.mp4")
# carVid=cv2.VideoCapture(0)

screen_width=carVid.get(3)
screen_height=carVid.get(4)
# print("Width====",carVid.get(3))
# print("Height===",carVid.get(4))
while True:
    dateTime=f"Width: {screen_width} Height:{screen_height}"
    res,frame=carVid.read()
    frame=cv2.resize(frame,(1000,600))
    text=f"Date: {datetime.datetime.now()}"
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font2=cv2.FONT_HERSHEY_TRIPLEX
    frame=cv2.putText(frame,text,(20,150),font,1,(0,0,255),1,cv2.LINE_AA)
    frame=cv2.putText(frame,dateTime,(50,50),font2,1,(0,0,255),1,cv2.LINE_AA)
    cv2.imshow("Askery",frame)
    if cv2.waitKey(30)==ord("q"):
        break
cv2.destroyAllWindows()
    
