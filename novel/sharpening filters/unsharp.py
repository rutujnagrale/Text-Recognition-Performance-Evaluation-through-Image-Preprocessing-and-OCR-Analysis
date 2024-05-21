import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Apply Gaussian blur to create a blurred version of the image
blurred_image = cv2.GaussianBlur(image, (5,5), 0)

# Calculate the sharpened image by subtracting the blurred image from the original
sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.1,0 )

# Display the original and sharpened images
##cv2.imshow('Original Image', image)
# cv2.imshow('Sharpened Image', sharpened_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image, sharpened_image]
label = ['Original Image', 'Unsharp Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()

