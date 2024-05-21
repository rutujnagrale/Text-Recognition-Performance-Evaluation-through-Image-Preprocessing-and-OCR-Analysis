import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5,5), 0)

# Define the Point Spread Function (PSF)
psf = np.ones((5, 5)) / 25

# Perform deconvolution using cv2.filter2D
restored_image = cv2.filter2D(blurred_image, -1, psf)

# Display the original and restored images
#cv2.imshow('Original Image', blurred_image)
# cv2.imshow('Restored Image (Deconvolution)', restored_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image, restored_image]
label = ['Original Image', 'Wiener Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
