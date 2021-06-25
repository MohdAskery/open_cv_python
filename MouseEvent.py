import cv2
import numpy as np

# def draw(event,x,y,flag,params):
#     print(f"event:{event}")
#     print(f"x : {x}")
#     print(f"y : {y}")
#     print(f"flag : {flag}")
#     print(f"params : {params}")
#     if event==cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(0,40,244),5)
#     if event==cv2.EVENT_RBUTTONDBLCLK:
#         cv2.rectangle(img,(x,y),(x+100,y+75),(0,0,255),3)
# cv2.namedWindow(winname="Board")
# img=np.ones([512,512,3])
# cv2.setMouseCallback("Board",draw)

# while True:
#     cv2.imshow("Board",img)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
li=[[0,0],[0,0]]
def mouse_event(event, x, y, flg, param):

    # print("event==",event)
    # print("x==",x)
    # print("y==",y)
    # print("flg==",flg)
    # print("param==",param)

    font=cv2.FONT_HERSHEY_PLAIN
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cord=f"X :{x} Y :{y}"
        co=[]
        co.append(x)
        co.append(y)
        li.append(co)
        cv2.putText(img,cord,(x,y),font,1,(0,0,255),2)
        
        del li[0]
    if event == cv2.EVENT_RBUTTONDOWN:

        b=img[x,y,0]
        g=img[x,y,1]
        r=img[x,y,2]
        print(img[x,y,0])
        print(img[x,y,1])
        print(img[x,y,2])
        color_bgr=f"bgr({b},{g},{r})"
        cv2.putText(img,color_bgr,(x,y),font,1,(0,0,255),2)

cv2.namedWindow(winname="Board")
img=cv2.imread("file.jpg")
img=cv2.resize(img,(900,600))
cv2.setMouseCallback("Board",mouse_event)
i=30
while True:
    sx,sy=li[0]
    ex,ey=li[1]
    
    img=cv2.line(img,(sx,sy),(ex,ey),(0,0,0),3)
    
    i+=1
    cv2.imshow("Board",img)
    

    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()