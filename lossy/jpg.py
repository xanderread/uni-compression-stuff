# jpeg compression from scratch

import cv2
import numpy as np
import sys

# take in path to og image
og_image_path = sys.argv[1]

#load image into open cv 
og_image = cv2.imread(og_image_path) 
#show og image 
cv2.imshow('original image',og_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#change colour space of image to YCbCr
ycc_image = cv2.cvtColor(og_image, cv2.COLOR_BGR2YCR_CB)

#split the ycb image into the 3 channles 
lum_channel, blue_chrom_channel, red_chrom_channel = cv2.split(ycc_image)

#show the channels
cv2.imshow('luminance channel', lum_channel)
cv2.imshow('chrominance blue channel', blue_chrom_channel)
cv2.imshow('chrominance red channel', red_chrom_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

#downsample the chromance channels (the human eye cant see these as well)

'''4:2:0 (Horizontal and Vertical Downsampling): This is the most common form of chroma downsampling used in consumer video and images, including formats like JPEG and H.264. It reduces the chrominance resolution by a factor of 2 both horizontally and vertically. For every 4 pixels (2x2), there are 4 samples of Y but only 1 sample of Cb and 1 sample of Cr.''' 

blue_chrom_channel = cv2.pyrDown(blue_chrom_channel) 
red_chrom_channel = cv2.pyrDown(red_chrom_channel)

# divide chanels into 8x8 blocks 
print(red_chrom_channel.shape)


