import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Apply Canny edge detector
edges = cv2.Canny(image, 100, 200)  # Adjust the thresholds as needed

# Display the original and edge-detected images
#cv2.imshow('Original Image', image)
# cv2.imshow('Canny Edge Detected Image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
display = [image, edges]
label = ['Original Image', 'Canny Edge']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
