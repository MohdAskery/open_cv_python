import cv2
import pafy

#Mobile Camera

url="https://www.youtube.com/watch?v=A24t8LTelN4"
data=pafy.new(url)
data= data.getbest()

video=cv2.VideoCapture(0,cv2.CAP_DSHOW)

video.open(data.url)

while video.isOpened():
    ret,frame=video.read()
    
    if ret:
        frame=cv2.resize(frame,(500,400))

        cv2.imshow("Video",frame)
        
        if cv2.waitKey(30)==ord("q"):
            break
        

video.release()
cv2.destroyAllWindows()