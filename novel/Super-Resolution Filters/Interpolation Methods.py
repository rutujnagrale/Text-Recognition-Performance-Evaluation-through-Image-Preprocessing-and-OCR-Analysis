import cv2

# Load a low-resolution image
lr_image = cv2.imread('original.jpg')

# Upscale the image using different interpolation methods
bicubic_upscale = cv2.resize(lr_image, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
nearest_upscale = cv2.resize(lr_image, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
lanczos_upscale = cv2.resize(lr_image, None, fx=1, fy=1, interpolation=cv2.INTER_LANCZOS4)

# Display the low-res and upscaled images
cv2.imshow('Low-Resolution Image', lr_image)
cv2.imshow('Bicubic Upscale', bicubic_upscale)
cv2.imshow('Nearest Neighbor Upscale', nearest_upscale)
cv2.imshow('Lanczos Upscale', lanczos_upscale)
cv2.waitKey(0)
cv2.destroyAllWindows()


