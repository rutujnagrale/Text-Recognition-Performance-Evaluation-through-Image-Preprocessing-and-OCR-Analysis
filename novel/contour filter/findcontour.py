import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection (you can use Canny or any other edge detection method)
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank image
contour_image = np.zeros_like(image)

cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the result
# cv2.imshow('Contours', contour_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

display = [image, contour_image]
label = ['Original Image', 'Contour Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
