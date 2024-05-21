from PIL import ImageEnhance, Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
## ****Best for original image with 300*400 pixels**** 

# Open an image
image = Image.open('original.jpg')

# Define color balance adjustment values (0.0 to 2.0, where 1.0 is no adjustment)
blue_gain = 2.5   # was 1.2
green_gain = 2.8  # was 0.8
red_gain = 1.5      # was 1.0

# Apply color balance adjustment
enhancer = ImageEnhance.Color(image)
adjusted_image = enhancer.enhance(blue_gain)

# Display the original and adjusted images
#image.show()
# adjusted_image.show()

display = display = [np.array(image), np.array(adjusted_image)]  # Convert to NumPy array
label = ['Original Image', 'Color Balance Adjustment']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(display[i], cmap='gray')  # Remove cv2.cvtColor, as it's already in RGB format
    plt.title(label[i])

plt.show()



