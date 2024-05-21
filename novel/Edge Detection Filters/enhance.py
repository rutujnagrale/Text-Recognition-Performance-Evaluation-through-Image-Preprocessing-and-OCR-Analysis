from PIL import Image, ImageEnhance, ImageFilter

def remove_dark_spots(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = image.convert("L")

    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(gray_image)
    enhanced_image = enhancer.enhance(1.5)  # Adjust the enhancement factor as needed

    # Apply a filter to reduce noise and blur
    blurred_image = enhanced_image.filter(ImageFilter.GaussianBlur(radius=2))

    # Save the result
    blurred_image.save(output_path)

# Example usage
input_path = "original.jpg"
output_path = "D:/project on filter/processed_image.jpg"


remove_dark_spots(input_path, output_path)
