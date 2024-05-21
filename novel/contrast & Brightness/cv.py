import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Define contrast and brightness values
contrast = 1.2  # was 1.5
brightness = 16  # was 10

# Apply contrast and brightness adjustments
adjusted_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)

# Display the original and adjusted images
#cv2.imshow('Original Image', image)
# cv2.imshow('Adjusted Image', adjusted_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image, adjusted_image]
label = ['Original Image', 'Contrast Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
