from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = plt.imread('original.png')

# Reshape the image to a 2D array of pixels
pixels = image.reshape((-1, 3))

# Convert to float32 for clustering
pixels = np.float32(pixels)

# Estimate the bandwidth (bandwidth controls the size of the kernel)
bandwidth = estimate_bandwidth(pixels, quantile=0.1, n_samples=500)  # Adjust quantile value


# Perform Mean Shift clustering
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(pixels)

# Retrieve the labels and cluster centers
labels = ms.labels_
cluster_centers = ms.cluster_centers_

# Assign each pixel to one of the clusters
segmented_image = cluster_centers[labels].reshape(image.shape)

# Display the result
plt.figure(figsize=(8, 4))

plt.subplot(121)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.axis('off')

plt.tight_layout()
plt.show()
