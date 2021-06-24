import cv2

img=cv2.imread("images/img0.png")
img=cv2.resize(img,(600,500))
img=cv2.line(img,(0,250),(600,250),(222,45,5),8)
cv2.imshow("image",img)


if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()
cv2.destroyAllWindows()