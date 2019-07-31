# -*- coding: utf-8 -*-
# @Date    : 2019-07-30 15:04:19
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import cv2
img = cv2.imread("C:/Users/EDZ/Desktop/test.png",1)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
#ord返回字符的十进制整数
elif k == ord('s'):
    cv2.imwrite("test2.png",img)
    cv2.destroyAllWindows()