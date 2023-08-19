import skimage.io as io
import skimage.color as color
import skimage.filters as filters
import skimage.segmentation as seg

# Load image
image = io.imread("C:\\Users\\SUTHAKARAN.P\\PycharmProjects\\fuirts\\image\\pear1.jpg")

# Convert to grayscale
gray_image = color.rgb2gray(image)

# Threshold image
thresh = filters.threshold_otsu(gray_image)
binary = gray_image > thresh

# Label regions
label_image = seg.label_expands(binary)

# Count regions
num_regions = label_image.max()

# Output results
print(f'Total number of affected regions: {num_regions}')
