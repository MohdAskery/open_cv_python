import cv2

video=cv2.VideoCapture(r"D:\openCV python\Image-Processing-Tutorials\Data\test2.mp4")

while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(500,400))
    
    fr=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    
    cv2.imshow("Video",frame)
    cv2.imshow("Video2",fr)
    
    k=cv2.waitKey(20)
    if k==ord("q"):
        break

cv2.destroyAllWindows()