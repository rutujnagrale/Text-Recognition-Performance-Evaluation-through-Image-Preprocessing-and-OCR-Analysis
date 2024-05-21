import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('D:/project on filter/novel/original.jpg')

# Apply Gaussian blur to reduce noise (optional but can be beneficial)
blurred = cv2.GaussianBlur(image, (3, 3), 0)

# Apply the Laplacian filter for edge enhancement
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

# Add the Laplacian image to the original image to sharpen it
sharpened = np.clip(image + laplacian, 0, 255).astype(np.uint8)

# Display the original and sharpened images
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
plt.title('Sharpened Image')
plt.axis('off')

plt.tight_layout()
plt.show()
