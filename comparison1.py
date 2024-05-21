from PIL import Image
import pytesseract

def image_text_quality(image_path):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Use pytesseract to perform OCR on the image
        extracted_text = pytesseract.image_to_string(img)
        #print(extracted_text)
        
        # Measure text length and readability
        #  metrics (you can add more metrics as needed)
        text_length = len(extracted_text)
        readability_score = 10 - text_length  # Example: simple metric based on text length
        
        return readability_score
    
    except IOError:
        print("Unable to load image.")
        return None

# Provide the file paths of the images you want to compare
image1_path = "D:/project on filter/original.jpg"
image2_path = "D:/project on filter/thelastoutput.jpg"

# Get text quality metrics for each image
text_quality1 = image_text_quality(image1_path)
#print(text_quality1)
text_quality2 = image_text_quality(image2_path)
#print(text_quality2)

if text_quality1 is not None and text_quality2 is not None:
    # Simple comparison based on readability score
    if text_quality1 > text_quality2:
        print("Image 1 has better text readability.")
    elif text_quality2 > text_quality1:
        print("Image 2 has better text readability.")
    else:
        print("Both images have similar text readability.")