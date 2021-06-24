import cv2

img=cv2.imread("file.jpg")
img=cv2.resize(img,(500,400))

# print(img)
cv2.imshow("Original",img)

img2=cv2.imread("file.jpg",-1)
img2=cv2.resize(img2,(500,400))

# print(img2)
cv2.imshow("Original2",img2)


img3=cv2.imread("file.jpg",0)
img3=cv2.resize(img3,(500,400))
# print(img3)

cv2.imshow("Original3",img3)

k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite('sav.png',img3)
cv2.destroyAllWindows()