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
	print(image_orig_name); print(image_lable_name)
	yes = []; no = []
	img_lable = imread(image_lable_name)
	img_orig = imread(image_orig_name)
	# print(img_lable.shape)
	yes = np.argwhere(img_lable == 19)
	no = np.argwhere(img_lable != 19)
	# print(yes)
	# for row in range(width):
	# 	for col in range(height):
	# 		if list(img_lable[row,col]) == [30,170,250]:
	# 			yes.append((row, col))
	# 		elif row > 40 and row < width - 40 and col > 40 and col < height - 40:
	# 			no.append((row, col))

	# random.shuffle(yes); random.shuffle(no)
	# print(yes); print(no)

	i = 1
	while len(yes) and i:
		i -= 1
		row, col = yes[0]
		# row, col = yes.pop()
		crop_img = img_orig[row-40:row+40, col-40:col+40]

		cv2.imshow('sample image',crop_img)
		cv2.waitKey(0) # waits until a key is pressed
		cv2.destroyAllWindows() # destroys the window showing image


	# print(random.sample(no, 10))

	# crop_img = img[y-40:y+40, x-40:x+40]



# getCorps('aachen_000015_000019_gtFine_color.png')

# cv2.imshow('sample image',img)

# cv2.waitKey(0) # waits until a key is pressed
# cv2.destroyAllWindows() # destroys the window showing image



train_lable_path = 'E:/excellenteam/CityScapes/gtFine/train'
train_orig_path = 'E:/excellenteam/CityScapes/leftImg8bit/train'

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