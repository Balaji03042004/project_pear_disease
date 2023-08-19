import imageio.v3 as iio
import matplotlib.pyplot as plt
import skimage.color

# read input image
image = iio.imread("C:\\Users\\SUTHAKARAN.P\\PycharmProjects\\fuirts\\image\\pear1.jpg")

# display original image
fig, ax = plt.subplots()
plt.imshow(image)

# convert to grayscale and display
gray_image = skimage.color.rgb2gray(image)
fig, ax = plt.subplots()
plt.imshow(gray_image, cmap="gray")