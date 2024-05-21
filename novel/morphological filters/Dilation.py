from skimage import io, morphology
from skimage.color import rgb2gray
import cv2
import matplotlib.pyplot as plt


# Load an image and convert to grayscale
image = io.imread('original.jpg')
gray_image = rgb2gray(image)

# Apply dilation
dilated_image = morphology.binary_dilation(gray_image)

# Display the original and dilated images
io.imshow_collection([gray_image, dilated_image])
io.show()

display = [image, dilated_image]
label = ['Original Image', 'Dilation Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
