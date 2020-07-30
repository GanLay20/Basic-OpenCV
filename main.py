# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:32:45 2020

@author: Mahendra
"""

import cv2 as cv
import numpy as np
import os

"""
Reading Image 
cv.imread(path,flag)
flag = 1....RGB image
     = 0....Grayscale Image
"""
# # Read image
# image = cv.imread("Original Photo3.jpg",0)
# # Show image
# cv.imshow("Original Photo",image)

# cv.waitKey(0)
# cv.destroyAllWindows()


"""
Color Splitting
cv.split()
cv.shape()
"""
# image = cv.imread("rgb.png")
# B,G,R = cv.split(image)

# cv.imshow("Original Photo",image)
# cv.waitKey(0)

# cv.imshow("Blue",B)
# cv.waitKey(0)

# cv.imshow("Green",G)
# cv.waitKey(0)

# cv.imshow("Red",R)
# cv.waitKey(0)

# cv.destroyAllWindows()


# image = cv.imread("image1.png",1)
# cv.imshow("RGB",image)
# print("Image Dimension" , image.shape)
# cv.waitKey(0)

# image1 = cv.imread("image1.png",0)
# cv.imshow("Grayscale",image1)
# print("Image Dimension",image1.shape)
# cv.waitKey(0)

# cv.destroyAllWindows()


# src = cv.imread("image1.png")
# print(src.shape)
# cv.imshow("Original Image",src)
# cv.waitKey(0)


# src[:,:,1] = np.zeros([src.shape[0],src.shape[1]])

# cv.imwrite("NOgreen.jpeg",src)
# cv.destroyAllWindows()


"""
Drawing Circle,Rectangle and line

cv.rectangle(image,start_point,end_point,color,thickness)
cv.circle(image,center_coordinate,radius,color,thickness)
"""

#image = cv.imread("test.jpg")
# pt1 = (100,200)
# pt2 = (300.250)
# color = (90,255,200)
# thickness = 3
# result = cv.rectangle(image,pt1 = (100,200),pt2 = (300,250),
#                       color = (9,255,200),thickness = -1)

# cv.imshow("Drawing Rectangle",result)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Drawing Circle

# image = cv.imread("test.jpg")
# center = (650,100)
# radius = 50
# color = (0,255,200)
# thickness = -1

# result = cv.circle(image,center,radius,color,thickness)

# cv.imshow("Drawing Circle",result)
# cv.waitKey(0)
# cv.destroyAllWindows

# Putting text on image

# image = cv.imread("test.jpg")
# result = cv.putText(image,text = "Good Afternoon",
#                     org = (300,200),
#                     fontFace = cv.FONT_HERSHEY_DUPLEX,
#                     fontScale = 1,
#                     color = (200,255,0),
#                     thickness = 3,
#                     lineType = cv.LINE_AA)


# cv.imshow("Putting Text",result)
# cv.waitKey(0)
# cv.destroyAllWindows

"""
Image Adding and Subtraction
cv.addWeighted(src1,alpha,src2,beta,gamma)
alpha,beta....the corresponding weights to be considered
              while performing the weighted addition
gamma = Measurement of light

dst = src1 * alpha + src2 * beta + gamma
"""


# image1 = cv.imread("44.jpg")
# cv.imshow("First Image",image1)
# cv.waitKey(0)
# image2 = cv.imread("55.jpg")
# cv.imshow("Second Image",image2)
# cv.waitKey(0)

# sum = cv.addWeighted(image1,0.8,image2,0.6,0)
# cv.imshow("Final Image",sum)
# cv.waitKey(0)
# cv.destroyAllWindows()

# image1 = cv.imread("star.jpg")
# cv.imshow("First Image",image1)
# cv.waitKey(0)
# image2 = cv.imread("star2.jpg")
# cv.imshow("Second Photo",image2)
# cv.waitKey(0)

# sub = cv.subtract(image1,image2)
# cv.imshow("Final Photo",sub)

# cv.waitKey(0)
# cv.destroyAllWindows()


"""
Image Blurring
Important types of Blurring
1. Gaussian Blurring   .....cv.GaussianBlur()
2. Median Blur         .....cv.medianBlur()
3. Bilateral Blur      .....cv.bilteralFilter()

"""

# image = cv.imread("MR image with salt and pepper noise.jpg")
# cv.imshow("Original Image",image)
# cv.waitKey(0)

# Gaussian Blurring

# gas=cv.GaussianBlur(image,(7,7),0)
# cv.imshow("Gaussian Blurring",gas)


#Median Blur

# median = cv.medianBlur(image,5)
# cv.imshow("Meidan Blurring",median)
# cv.waitKey(0)
# cv.destroyAllWindows


#Bilateral Blur

# result = cv.bilateralFilter(image,9,75,75)
# cv.imshow("Bilateral Blurring",result)
# cv.waitKey(0)
# cv.destroyAllWindows


"""
Image Resize
Image Translation
Image Rotation

"""
# image = cv.imread('44.jpg')
# cv.imshow("Original Photo",image)
# cv.waitKey(0)

# scale = 30

# width = int((image.shape[0] * scale / 100))
# height = int((image.shape[1] * scale / 100))

# size = (width,height)

# output = cv.resize(image,size)
# cv.imwrite("Output.jpg",output)
# cv.imshow("Resize Image",output)
# cv.waitKey(0)
# cv.destroyAllWindows

# image = cv.imread('44.jpg')
# cv.imshow("Original Photo",image)
# cv.waitKey(0)


# #width = 200
# height = 800

# #size = (image.shape[1],width)
# size = (image.shape[0],height)
# output = cv.resize(image,size)

# cv.imshow("Resize Image",output)
# cv.waitKey(0)
# cv.destroyAllWindows

"""
Image Translation
1. Hiding a part of image
2. Cropping an Image
3. Shifting an image

cv.warpAffine
cv.getRotationMatrix2D()
"""

# image = cv.imread("44.jpg")
# cv.imshow("Original Photo",image)

# cv.waitKey(0)

# width = int(image.shape[0])
# height = int(image.shape[1])

# new_width = width / 4
# new_height = height / 4

# T = np.float32([[1,0,new_width],[0,1,new_height]])
# image_translate = cv.warpAffine(image,T,(width,height))

# cv.imshow("Translation ",image_translate)
# cv.waitKey(0)
# cv.destroyAllWindows()



# image = cv.imread("44.jpg")
# cv.imshow("Original Photo",image)

# cv.waitKey(0)

# width = int(image.shape[0])
# print("Width",width)
# height = int(image.shape[1])
# print("Height",height)

# D = cv.getRotationMatrix2D((width/2  ,height/2 ),30,1)
# image_rotate = cv.warpAffine(image,D,(width,height))

# cv.imshow("Rotation ",image_rotate)
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
Edge Detection
Canny Filter

# cv.Canny
# """

# image = cv.imread("44.jpg")
# cv.imshow("Original Image",image)
# cv.waitKey(0)

# edges = cv.Canny(image,100,200)
# cv.imshow("Edge Detection",edges)
# cv.waitKey(0)
# cv.destroyAllWindows()

# camera = cv.VideoCapture("rica.mp4")

# try :
#     if not os.path.exists("data"):
#         os.mkdir('data')
# except OSError:
#     print("Error : Creating directory of data")

# current_frame = 0

# while True:
#     ret,frame = camera.read()
    
#     if ret:
#         name = './data/frame' + str(current_frame) + '.jpg'
#         print("Creating...." + name)
#         cv.imwrite(name,frame)
        
#         current_frame +=1
#     else:
#         break
    
# camera.release()
# cv.destroyAllWindows()
