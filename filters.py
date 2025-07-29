from PIL import Image, ImageFilter
import numpy as np
import scipy.ndimage

# === Basic Filters ===

def mean_filter(image):
    return image.filter(ImageFilter.BoxBlur(1))

def median_filter(image):
    return image.filter(ImageFilter.MedianFilter(3))

def gaussian_filter(image):
    return image.filter(ImageFilter.GaussianBlur(1))

# === Extra Filters ===

def grayscale_filter(image):
    return image.convert("L").convert("RGB")  # Convert to grayscale and back to RGB for consistency

def laplacian_filter(image):
    gray = image.convert("L")
    np_img = np.array(gray, dtype=np.float32)

    # Apply Laplacian kernel
    laplacian_kernel = [[0, 1, 0],
                        [1, -4, 1],
                        [0, 1, 0]]
    edge_img = scipy.ndimage.convolve(np_img, laplacian_kernel)

    # Normalize and convert back to image
    edge_img = np.clip(edge_img, 0, 255).astype(np.uint8)
    return Image.fromarray(edge_img).convert("RGB")

def highpass_filter(image):
    gray = image.convert("L")
    np_img = np.array(gray, dtype=np.float32)

    # High-pass filter kernel
    highpass_kernel = [[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]]
    highpass_img = scipy.ndimage.convolve(np_img, highpass_kernel)

    # Normalize and convert back to image
    highpass_img = np.clip(highpass_img, 0, 255).astype(np.uint8)
    return Image.fromarray(highpass_img).convert("RGB")

# === Filter Selector ===

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)

    if filter_type == 'mean':
        image = mean_filter(image)
    elif filter_type == 'median':
        image = median_filter(image)
    elif filter_type == 'gaussian':
        image = gaussian_filter(image)
    elif filter_type == 'grayscale':
        image = grayscale_filter(image)
    elif filter_type == 'laplacian':
        image = laplacian_filter(image)
    elif filter_type == 'highpass':
        image = highpass_filter(image)
    else:
        return image_path  # Unknown filter, return original

    # Save new image with "_filtered" suffix
    filtered_image_path = image_path.replace(".png", "_filtered.png")
    image.save(filtered_image_path)
    return filtered_image_path
