from skimage import io, morphology
from skimage.color import rgb2gray
import cv2
import matplotlib.pyplot as plt

# Load an image and convert to grayscale
image = io.imread('original.jpg')
gray_image = rgb2gray(image)

# Apply opening
opened_image = morphology.binary_opening(gray_image)

# Display the original and opened images
io.imshow_collection([gray_image, opened_image])
io.show()

display = [image, opened_image]
label = ['Original Image', 'Opening Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
