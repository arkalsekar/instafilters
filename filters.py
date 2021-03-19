import numpy as np
import streamlit as st 
import cv2
import copy
import imutils
import PIL
from PIL import Image
from scipy.interpolate import UnivariateSpline

# This Loads the Image
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# GraySclaing the Image
def grayImage(image):    
    img = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
    return img

# Getting the Edges of Image
def Edge(image):
    return cv2.Canny(image, 100, 150)

# Blurring the Image
def gaussianBlur(image):
    return cv2.GaussianBlur(image, (35, 35), 0)

# Spread  Lookup for x and y
def spreadLookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))

# Applying Warm Filter to the Image
def warmImage(image):
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    return cv2.merge((red_channel, green_channel, blue_channel))

# Applying Cold Filter to the Image
def coldImage(image):
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(image)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    return cv2.merge((red_channel, green_channel, blue_channel))    

def resize(image, left, top, right, bottom):

    ima = image.crop((left, top, right, bottom))
    resized = np.array(ima)
    return resized
