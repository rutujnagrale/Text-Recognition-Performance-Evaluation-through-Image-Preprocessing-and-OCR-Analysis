import cv2
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Apply Bilateral filter
blurred_image = cv2.bilateralFilter(image, 15, 100, 100)  ## was 65 , 65

# Display the original and blurred images
# cv2.imshow('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.resizeWindow('Blurred Image', blurred_image.shape[1], blurred_image.shape[0])

# Display using matplotlib
display = [image, blurred_image]
label = ['Original Image', 'Bilateral Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
