import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg')

# Apply Median blur
blurred_image = cv2.medianBlur(image, 3)  # was 5 now 3

# Display the original and blurred images
#cv2.imshow('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

display = [image, blurred_image]
label = ['Original Image', 'Median Blur']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
