# # from matplotlib import pyplot
# import cv2
import random
import os
import cv2
import numpy as np
from imageio import imread

train_lable_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/gtFine/train'
train_orig_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/leftImg8bit/train'

output_image = list()
output_lable = list()

def getCorps(image_lable_name ,image_orig_name):
	global output_image, output_lable
	# print(image_orig_name);
	print(image_lable_name)
	img_lable = imread(image_lable_name)
	img_orig = imread(image_orig_name)
	width, height = img_lable.shape
	yes = np.argwhere(img_lable[41:height-41,41:width-41] == 19)+40
	no = np.argwhere(img_lable[41:height-41,41:width-41] != 19)+40

	for _ in range(1):
		if len(yes):
			row, col = yes[random.randint(0, len(yes)-1)]
			crop_img = img_orig[row-40:row+40, col-40:col+40]
			output_image.append(crop_img)
			output_lable.append( 1)
		if len(no):
			row, col = no[random.randint(0, len(no)-1)]
			crop_img = img_orig[row-40:row+40, col-40:col+40]
			output_image.append(crop_img)
			output_lable.append(0)
		if not len(yes) and not len(no):
			break
	# print(output_image); print(output_lable)

lable_images = {}; orig_image = {}

for r, d, f in os.walk(train_lable_path):
	for file in f:
		if 'labelIds' in file:
			lable_images[''.join(file.split('_')[:3])] = os.path.join(r, file)
			

for r, d, f in os.walk(train_orig_path):
	for file in f:
		orig_image[''.join(file.split('_')[:3])] = os.path.join(r, file)
	

# for name_lable, path_lable in lable_images.items():
# 	getCorps(path_lable, orig_image[name_lable])

getCorps("E:/Excellenteam-Brosh/course/GitHub/CityScapes/gtFine/train/aachen/aachen_000007_000019_gtFine_labelIds.png", "E:/Excellenteam-Brosh/course/GitHub/CityScapes/leftImg8bit/train/aachen/aachen_000007_000019_leftImg8bit.png")


# from array import array

output_file = open('output_image', 'wb')
for arr in output_image:
	arr.astype('uint8').tofile("output_image")
# float_array = array('d', output_image)
# float_array.tofile(output_file)
output_file.close()

# output_file = open('output_lable', 'wb')
# float_array = array('d', output_lable)
# float_array.tofile(output_file)
# output_file.close()