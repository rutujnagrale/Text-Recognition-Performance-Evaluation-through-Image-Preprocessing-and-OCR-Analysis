import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Apply Laplacian filter
laplacian_image = cv2.Laplacian(image, cv2.CV_64F)

# Convert the result back to uint8
laplacian_image = cv2.convertScaleAbs(laplacian_image)

# Display the original and Laplacian-filtered images
#cv2.imshow('Original Image', image)


display = [image, laplacian_image]
label = ['Original Image', 'Laplacian Sharpening Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
