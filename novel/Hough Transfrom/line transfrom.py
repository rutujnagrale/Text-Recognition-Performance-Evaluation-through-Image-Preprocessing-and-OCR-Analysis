import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load an image
new = cv2.imread('original.png')
image = cv2.imread('original.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection (you can use Canny or any other edge detection method)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Apply Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Draw detected lines on the original image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the result
display = [new, image]
label = ['Original Image', 'Line Transform']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
