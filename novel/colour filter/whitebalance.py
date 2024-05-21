from PIL import ImageOps, Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
##   *****best for original image with 300 * 400 pixels**********

# Open an image
image = Image.open('original.jpg')

# Perform auto white balance correction
corrected_image = ImageOps.autocontrast(image, cutoff=7) # was 5

# Display the original and white balance corrected images
#image.show()
# corrected_image.show()

display = display = [np.array(image), np.array(corrected_image)] 
label = ['Original Image', 'White Balance Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(display[i], cmap='gray')  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()


