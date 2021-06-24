#Askdkkd ddk
import cv2

video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("outputGray.avi",fourcc,20.0,(640,480),0)

while video.isOpened():
    ret,frame=video.read()
    
    if ret:
        frame=cv2.resize(frame,(500,400))
        fr=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        
        cv2.imshow("Video",frame)
        cv2.imshow("Video2",fr)
        
        output.write(fr)
        
        if cv2.waitKey(1)==ord("q"):
            break
        

video.release()
output.release()
cv2.destroyAllWindows()