from skimage import io, morphology
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import cv2

# Load an image and convert to grayscale
image = io.imread('original.jpg')
gray_image = rgb2gray(image)

# Apply closing
closed_image = morphology.binary_closing(gray_image)

# Display the original and closed images
io.imshow_collection([gray_image, closed_image])
io.show()


display = [image, closed_image]
label = ['Original Image', 'Closing Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
