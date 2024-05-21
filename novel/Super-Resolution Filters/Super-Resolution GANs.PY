import tensorflow as tf
import cv2
from tensorflow.python.keras.applications import EDSR

# Load a low-resolution image
lr_image = cv2.imread('original.png')

# Load the pre-trained EDSR model
edsr_model = EDSR(weights='edsr')
edsr_model.summary()

# Upscale the image using the EDSR model
sr_image = edsr_model.predict(tf.expand_dims(lr_image, axis=0))

# Display the low-res and super-res images
cv2.imshow('Low-Resolution Image', lr_image)
cv2.imshow('Super-Resolution Image', sr_image[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
