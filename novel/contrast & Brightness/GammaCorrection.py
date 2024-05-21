from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Open an image
image = Image.open('D:/project on filter/novel/original.jpg')

# Define contrast and brightness values
contrast = 1.3  # was 1.5
brightness = 1.3  # was 1.5

# Apply contrast adjustment
enhancer = ImageEnhance.Contrast(image)
image_contrast = enhancer.enhance(contrast)

# Apply brightness adjustment
enhancer = ImageEnhance.Brightness(image_contrast)
adjusted_image = enhancer.enhance(brightness)

# Display the original and adjusted images
#image.show()
# adjusted_image.show()

display = [np.array(image), np.array(adjusted_image)]  # Convert to NumPy array
label = ['Original Image', 'Gamma Correction']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(display[i], cmap='gray')  # Remove cv2.cvtColor, as it's already in RGB format
    plt.title(label[i])
    
plt.show()
