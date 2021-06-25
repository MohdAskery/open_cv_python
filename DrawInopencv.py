import cv2
import numpy as np

# img=cv2.imread("images/img0.png")
# img=cv2.resize(img,(600,500))
# img=np.zeros([512,512,3])
img=np.ones([512,512,10])
img=cv2.line(img,(0,250),(600,250),(222,45,5),3)
img=cv2.arrowedLine(img,(0,20),(600,250),(222,45,5),3)
img=cv2.rectangle(img,(500,500),(300,300),(0,0,255),3)
img=cv2.circle(img,(100,100),60,(0,0,255),3)
font=cv2.FONT_ITALIC
img=cv2.putText(img,"Askery",(180,150),font,2,(0,230,235),3,cv2.LINE_AA)
img=cv2.ellipse(img,(340,300),(100,300),0,0,(360),55,4)
cv2.imshow("image",img)


if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()
cv2.destroyAllWindows()