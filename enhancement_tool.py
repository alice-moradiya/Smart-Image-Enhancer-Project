import cv2
import numpy as np

def adjust_brightness_contrast(image, brightness=0, contrast=0):
    """
    Adjusts the brightness and contrast of an image.
    :param image: Input image
    :param brightness: Brightness adjustment factor
    :param contrast: Contrast adjustment factor
    """
    # Convertes to float to prevent clipping issues
    img_float = image.astype(np.float)
    
    # Adjust brightness and contrast
    img_bright_contrast = np.clip((1 + contrast / 100.0) * img_float + brightness, 0, 255)
    
    # Convert back to original data type
    enhanced_img = img_bright_contrast.astype(np.uint8)
    return enhanced_img

if __name__ == "__main__":
    img_path = 'image1.jpg'
    image = cv2.imread(img_path)

    # Enhancing the image
    bright_contrast_img = adjust_brightness_contrast(image, brightness=30, contrast=50)
    
    