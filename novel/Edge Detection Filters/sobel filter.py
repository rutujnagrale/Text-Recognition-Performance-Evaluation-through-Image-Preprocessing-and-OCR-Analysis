import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg')

# Apply the Sobel filter for edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Calculate the gradient magnitude
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Normalize the gradient magnitude to the range [0, 255]
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Convert to 8-bit unsigned integer
gradient_magnitude = np.uint8(gradient_magnitude)

# Display the original and edge-detected images
#cv2.imshow('Original Image', image)
# cv2.imshow('Edge Detected Image', gradient_magnitude)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image, gradient_magnitude]
label = ['Original Image', 'Sober Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()

