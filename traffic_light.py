import random
import os
import numpy as np
from imageio import imread
from matplotlib import pyplot as plt

lable_images = {}; orig_image = {}

train_lable_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/gtFine/train'
train_orig_path = 'E:/Excellenteam-Brosh/course/GitHub/CityScapes/leftImg8bit/train'

# ==========================================================================================

def getPaths(lable_images, orig_image):

	for r, d, f in os.walk(train_lable_path):
		for file in f:
			if 'labelIds' in file:
				lable_images[''.join(file.split('_')[:3])] = os.path.join(r, file)

	for r, d, f in os.walk(train_orig_path):
		for file in f:
			orig_image[''.join(file.split('_')[:3])] = os.path.join(r, file)

# ==========================================================================================

def crop_image(src, lst, label, data_file, labels_file):
	row, col = lst[random.randint(0, len(lst)-1)]
	data_file.write(bytearray(src[row-40:row+40, col-40:col+40]))
	labels_file.write(bytes(label.encode('charmap')))

# ==========================================================================================

def run():

	with open('data.bin', 'wb') as data, open('labels.bin', 'wb') as labels:

		for name_lable, path_lable in lable_images.items():

			if 'jena' in name_lable:

				img_lable = imread(path_lable);
				img_orig = imread(orig_image[name_lable])

				width, height = img_lable.shape
				yes = np.argwhere( img_lable[41:height-41, 41:width-41] == 19 ) + 40
				no = np.argwhere( img_lable[41:height-41, 41:width-41] != 19 ) + 40

				for _ in range(1):
					if len(yes):
						crop_image(img_orig, yes, '1', data, labels)
					if len(no):
						crop_image(img_orig, no, '0', data, labels)
					if not len(yes) and not len(no):
						break

# ==========================================================================================

def show_sample(fname, idx, crop_size):
	# face_from_raw = np.fromfile(fname, dtype=np.uint8)
	fp = np.memmap(fname, dtype='uint8', offset=idx*(81*81*3), shape=(crop_size, crop_size, 3))
	with open('labels.bin', 'r') as labelsfile:
		print(labelsfile.read(idx))
	plt.imshow(fp)
	plt.show()

# ==========================================================================================

if __name__ == '__main__':
	getPaths(lable_images, orig_image)
	run()
	show_sample('data.bin', 3, 81)