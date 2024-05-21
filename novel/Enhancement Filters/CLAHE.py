import cv2
import matplotlib.pyplot as plt
# Load an image
image1 = cv2.imread('original.jpg')
image = cv2.imread('original.jpg', cv2.IMREAD_GRAYSCALE)


# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=1.1, tileGridSize=(23, 20))  # was 2 , 8 , 8
clahe_output = clahe.apply(image)

# Display the original and CLAHE-enhanced images
#cv2.imshow('Original Image', image)
# cv2.imshow('CLAHE Enhanced Image', clahe_output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


display = [image1, clahe_output]
label = ['Original Image', 'CLAHE']

fig = plt.figure(figsize=(12, 10))

for i in range(len(display)):
    fig.add_subplot(1, 2, i+1)
    plt.imshow(cv2.cvtColor(display[i], cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.title(label[i])

plt.show()