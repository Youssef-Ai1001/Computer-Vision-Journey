"""
Reinhard color transfer 

This approach is suitable for stain normalization of pathology images where
the 'look and feel' of all images can be normalized to a template image. 
This can be a good preprocessing step for machine learning and deep learning 
of pathology images. 

"""
import cv2 as cv
import numpy as np
import os

input_dir = '/home/sir-youssef/Coding/Computer Vision/images/input_images/'
input_img_list = os.listdir(input_dir)

output_dir = '/home/sir-youssef/Coding/Computer Vision/images/output_images/'

style_dir = '/home/sir-youssef/Coding/Computer Vision/images/style_images/'
style_img_list = os.listdir(style_dir)

def get_maen_and_std(x):
    x_mean , x_std = cv.meanStdDev(x)
    x_mean = np.hstack(np.around(x_mean,2))
    x_std = np.hstack(np.around(x_std,2))
    return x_mean,x_std

# DeFine Style image
style_img = cv.imread("/home/sir-youssef/Coding/Computer Vision/images/style_images/ocean_sunset.jpg")
style_img = cv.cvtColor(style_img,cv.COLOR_BGR2LAB)
style_img_mean ,style_img_std = get_maen_and_std(style_img)

for img in (input_img_list):
    # print(img)
    input_img = cv.imread(input_dir+img)
    # input_img = cv.imread(os.path.join(input_dir, img))
    input_img = cv.cvtColor(input_img,cv.COLOR_BGR2LAB)
    
    input_img_mean , input_img_std = get_maen_and_std(input_img)
    
    height, width, channel = input_img.shape
    
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,channel):
                x = input_img[i,j,k]
                # print(x)
                x = ((x-input_img_mean[k]) * (style_img_mean[k] / input_img_std[k])) + style_img_mean[k]
                x = round(x)
                # boundary check
                x = 0 if x < 0 else x
                x = 255 if x > 255 else x
                input_img[i,j,k] = x

    input_img = cv.cvtColor(input_img,cv.COLOR_LAB2BGR)
    cv.imwrite(output_dir+"modified style_"+img,input_img)