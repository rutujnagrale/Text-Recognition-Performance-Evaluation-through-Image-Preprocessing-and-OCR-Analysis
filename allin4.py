import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/1.jpg')

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
#                                      k = 5 * 5  , SD = 0 ;
# Calculate the sharpened image by subtracting the blurred image from the original
sharpened_image = cv2.addWeighted(image, 1.5, blurred_image, -0.7, 0)

# Apply Bilateral filter
blurred_image = cv2.bilateralFilter(
    sharpened_image, 15, 100, 100)  # was 65 , 65
                                    # dia = 9 , sigmacolour , sigmaspace
image2 = blurred_image
# Reshape the image to a 2D array of pixels
pixels = image2.reshape((-1, 3))

# Convert to float32 for K-means clustering
pixels = np.float32(pixels)

# Define the number of clusters (segments) you want
num_clusters = 3  # was 5

# Apply K-means clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(
    pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert the centers back to uint8
centers = np.uint8(centers)

# Assign each pixel to one of the clusters
segmented_image = centers[labels.flatten()].reshape((image.shape))


display = [image, segmented_image]
label = ['Original Image', 'K-mean Clustering Filter']
# Save the segmented image
cv2.imwrite('segmented_image3.jpg', segmented_image)


fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    # Convert BGR to RGB for matplotlib
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))
    plt.title(label[i])

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
