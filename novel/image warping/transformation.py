import cv2
import numpy as np

# Load your image
image = cv2.imread('original.jpg')

# Define the four corners of the region of interest (ROI) in the original image
original_points = np.float32([[13, 53], [280, 30], [15, 370], [285, 370]]) 
# was [50, 50], [300, 50], [50, 300], [300, 300]]

# Define the four corners of the desired transformed ROI
transformed_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])
# was [0, 0], [400, 0], [0, 400], [400, 400]]

# Compute the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(original_points, transformed_points)

# Apply the perspective transformation
warped_image = cv2.warpPerspective(image, perspective_matrix, (300, 400)) # was (400, 400)

# Display the result
cv2.imshow('Warped Image', warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
