import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('original.jpg')

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (9,9), 0) ## was 5 , 5

# Display the original and blurred images
##cv2.imshow('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image, blurred_image]
label = ['Original Image', 'Gaussian']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
