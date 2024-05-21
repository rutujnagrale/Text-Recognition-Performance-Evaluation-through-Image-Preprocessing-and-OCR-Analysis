import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise (optional but recommended)
blurred = cv2.GaussianBlur(image, (9, 9), 2)

# Apply Hough Circle Transform
circles = cv2.HoughCircles(
    blurred, 
    cv2.HOUGH_GRADIENT, dp=10, minDist=20, param1=50, param2=30, minRadius=5, maxRadius=100)

# Draw detected circles on the original image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)

# Display the result
# cv2.imshow('Hough Circles', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

display = [image, image]
label = ['Original Image', 'Bilateral Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()