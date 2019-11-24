# # from matplotlib import pyplot
# import cv2

# # print(pyplot.imread('aachen_000000_000019_gtFine_color.png'))

# print(cv2.imread('aachen_000000_000019_gtFine_color.png'))


import random
import os
import cv2
import numpy as np
from imageio import imread




# def crop(img):




def getCorps(image_lable_name ,image_orig_name):
	# print(image_orig_name); print(image_lable_name)
	img_lable = imread(image_lable_name)
	img_orig = imread(image_orig_name)
	width, height = img_lable.shape
	yes = np.argwhere(img_lable[41:height-41,41:width-41] == 19)+40
	no = np.argwhere(img_lable[41:height-41,41:width-41] != 19)+40

	for _ in range(1):
		if len(yes) == 0:
			break
		# while row 
		# row, col = yes[0]
		row, col = yes[random.randint(0, len(yes))]
		# row, col = yes.pop()
		crop_img = img_orig[row-40:row+40, col-40:col+40]
		# crop_img[38:42, 38:42] = 0
		# print(row, col)

		# cv2.imshow('sample image',crop_img)
		# cv2.waitKey(0) # waits until a key is pressed
		# cv2.destroyAllWindows() # destroys the window showing image


	# print(random.sample(no, 10))

	# crop_img = img[y-40:y+40, x-40:x+40]



# getCorps('aachen_000015_000019_gtFine_color.png')

# cv2.imshow('sample image',img)

# cv2.waitKey(0) # waits until a key is pressed
# cv2.destroyAllWindows() # destroys the window showing image



train_lable_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/gtFine/train'
train_orig_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/leftImg8bit/train'

# name = "berlin_000000_000019_gtFine_labelIds.png"
# def crop(path_image):


# with open(name, 'r') as f:
# 	print(f.readlines())

lable_images = {}; orig_image = {}

for r, d, f in os.walk(train_lable_path):
	for file in f:
		if 'labelIds' in file:
			lable_images[''.join(file.split('_')[:3])] = os.path.join(r, file)

for r, d, f in os.walk(train_orig_path):
	for file in f:
			orig_image[''.join(file.split('_')[:3])] = os.path.join(r, file)

for name_lable, path_lable in lable_images.items():
	getCorps(path_lable, orig_image[name_lable])

# for f in labled_images:
	# print(f)


# import glob


# def main():
# 	for filename in glob.glob('*.txt'):
# 	   # do your stuff
# if __name__ == '__main__':
# 	main()