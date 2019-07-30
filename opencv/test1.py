# -*- coding: utf-8 -*-
# @Date    : 2019-07-30 15:04:19
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import cv2
img = cv2.imread("C:/Users/Administrator/Desktop/test.jpg")
cv2.namedWindow("image") #创建窗口并显示的是图像类型
cv2.imshow("image",img)
cv2.waitKey(0)        #等待事件触发，参数0表示永久等待
cv2.destroyAllWindows()   #释放窗口