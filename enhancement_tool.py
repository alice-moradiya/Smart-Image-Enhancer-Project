import cv2
import numpy as np


def adjust_brightness(image, brightness=0):
    if image is None:
        raise ValueError("Invalid image provided for brightness adjustment.")

    # Ensuring the brightness shift is within the valid range [0, 255]
    brightness = np.clip(brightness, -255, 255)

    if brightness > 0:
        shadow = brightness
        highlight = 255
    else:
        shadow = 0
        highlight = 255 + brightness

    alpha_b = (highlight - shadow) / 255
    gamma_b = shadow

    # Adding the brightness value using the addWeighted function to prevent overflow
    brightness_img = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    return brightness_img


def adjust_contrast(image, contrast=1.0):
    if image is None:
        raise ValueError("Invalid image provided for contrast adjustment.")

    # Ensuring the contrast factor is within a reasonable range
    contrast = np.clip(contrast, 0.0, 3.0)  # 3.0 as an upper reasonable limit

    f = 131 * (contrast - 1) / 127 + 1  # Factor for adjusting contrast
    alpha_c = f
    gamma_c = 127 * (1 - f)

    # Scaling the pixel values using the addWeighted function to prevent overflow
    contrast_img = cv2.addWeighted(image, alpha_c, image, 0, gamma_c)
    return contrast_img


def adjust_sharpness(image):
    if image is None:
        raise ValueError("Invalid image provided for sharpening.")

    # Defining a sharpening kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    # Applying the sharpening kernel to the image using filter2D
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    return sharpened_image


def main():
    img_path = r'img2.png'
    image = cv2.imread(img_path)

    if image is None:
        print("Could not load the image.")
        return

    user_choice = input("Do you want to adjust brightness, contrast, & sharpness? (Enter 'b', 'c', 's'): ").lower()

    if user_choice not in ['b', 'c', 's']:
        print("Invalid choice. Please enter 'brightness' or 'contrast'.")
        return

    if user_choice == 'b':
        value = int(input("Enter the brightness value (negative to decrease, positive to increase) (ex. -1 or 2 or 3): "))
        x = adjust_brightness(image, brightness=value)
    elif user_choice == 'c':
        value = float(input("Enter the contrast value (less than 1 to decrease, greater than 1 to increase, 1 for no change): "))
        x = adjust_contrast(image, contrast=value)
    else:
        # no value for sharpness considering complications of matrix
        x = adjust_sharpness(image)

    # Saving the enhanced image
    cv2.imwrite('enhanced_image.jpg', x)
    print("Enhancement applied successfully.")


if __name__ == "__main__":
    main()
