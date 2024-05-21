import cv2
import matplotlib.pyplot as plt

# Load a noisy image
noisy_image = cv2.imread('original.jpg')

# Convert the image to grayscale for denoising
gray_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2GRAY)

# Apply Non-Local Means Denoising
denoised_image = cv2.fastNlMeansDenoising(gray_image, None, h=11, searchWindowSize=25) # was 10 and 21

# Display the noisy and denoised images
#cv2.imshow('Noisy Image', noisy_image)
# cv2.imshow('Denoised Image', denoised_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

display = [noisy_image, denoised_image]
label = ['Original Image', 'Denoising Filter']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()
