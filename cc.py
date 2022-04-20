1.import cv2
BGR_image=cv2.imread('1.png')
cv2.imshow('BGR_Image',BGR_image)
hsv_image=cv2.cvtColor(BGR_image,cv2.COLOR_BGR2HSV)
cv2.imshow('212221240047',hsv_image)
cv2.imwrite('hsv.jpg',hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
2.import cv2
HSV_image=cv2.imread('1.png')
cv2.imshow('HSV_Image',HSV_image)
#HSV2BGR
bgr_image=cv2.cvtColor(HSV_image,cv2.COLOR_HSV2BGR)
cv2.imshow('212221240047',bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
3.import cv2
BGR_image=cv2.imread('1.png')
cv2.imshow('BGR_Image',BGR_image)
#BGR2YCrCb
YCrCb_image=cv2.cvtColor(BGR_image,cv2.COLOR_BGR2YCrCb)
cv2.imshow('212221240047',YCrCb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
4.import cv2
BGR_image=cv2.imread('1.png')
blue=BGR_image[:,:,0]
green=BGR_image[:,:,1]
red=BGR_image[:,:,2]
cv2.imshow('BGR_Blue',blue)
cv2.imshow('BGR_Green',green)
cv2.imshow('BGR_Red',red)
merge_bgr=cv2.merge((blue,green,red))
cv2.imshow('212221240047',merge_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
5.import cv2
house_color_image=cv2.imread('hsv.jpg')
h, s, v = cv2.split(hsv_image)
cv2.imshow('h',h)
cv2.imshow('s',s)
cv2.imshow('v',v)
merge_hsv=cv2.merge((h,s,v))
cv2.imshow('212221240047',merge_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()