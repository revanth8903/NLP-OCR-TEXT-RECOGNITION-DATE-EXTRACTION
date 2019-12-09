#!/usr/bin/env python
# coding: utf-8

import cv2
import wand
import pytesseract
import pandas as pd
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import re


import glob
from PIL import Image
import pytesseract
new=[]
count=-1
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
for img in glob.glob("D:\Revanth\Receipts/*.jpeg"):
    count=count+1
    # Create an image object of PIL library
    image = Image.open(img)

    # pass image into pytesseract module
    # pytesseract is trained in many languages
    image_to_text = pytesseract.image_to_string(image, lang='eng')
    new.append(image_to_text)


new1=[]
new2=[]
for i in new:
    text=re.sub("\n"," ",i)
    new1.append(text)
for j in new1:
    match = re.search('(\d+/\d+/\d+)',j)
    new2.append(match)


for g in new2:
    if g==None:
        print('no')
    else:
        print(g.group())


count1=-1
count2=-1
for g in new2:
    if g==None:
        count1=count1+1
        print('No')
    else:
        count2=count2+1
        print('Yes')


a1=count1/2
a1

a2=count2/2
a2


total=a1+a2
total

accuracy=a2/total*100
accuracy

