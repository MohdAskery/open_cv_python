import cv2



vid=cv2.VideoCapture("D:\\openCV python\\muuuu (online-video-cutter.com).mp4")

res,frame=vid.read()
i=0
while True:
    if res:
        name=f"images/img{i}.png"
        cv2.imwrite(name, frame)
        vid.set(cv2.CAP_PROP_POS_MSEC,(10))
        res,frame=vid.read()
        frame=cv2.resize(frame,(400,300))
        cv2.imshow("Askery",frame)
        print(i)
        i+=1
        
        if cv2.waitKey(1)==ord("q"):
            break
    
vid.release()
cv2.destroyAllWindows()
    
