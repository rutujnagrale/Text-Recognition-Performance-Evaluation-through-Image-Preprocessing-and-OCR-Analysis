from skimage import io, morphology
from skimage.color import rgb2gray
import cv2
import matplotlib.pyplot as plt

# Load an image and convert to grayscale
image = io.imread('original.jpg')
gray_image = rgb2gray(image)

# Apply erosion
eroded_image = morphology.binary_erosion(gray_image)

# Display the original and eroded images
io.imshow_collection([gray_image, eroded_image])
io.show()

display = [image, eroded_image ]
label = ['Original Image', 'Erosion Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()