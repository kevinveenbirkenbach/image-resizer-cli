import os
from PIL import Image
import argparse

def resize_image(image_path, percentage, max_width, max_height, max_size, output_path):
    try:
        with Image.open(image_path) as img:
            # Resize by percentage or max dimensions
            if percentage:
                new_size = (int(img.width * percentage / 100), int(img.height * percentage / 100))
            elif max_width and max_height:
                aspect_ratio = min(max_width / img.width, max_height / img.height)
                new_size = (int(img.width * aspect_ratio), int(img.height * aspect_ratio))
            else:
                new_size = (img.width, img.height)

            img_resized = img.resize(new_size, Image.ANTIALIAS)

            # Adjust quality to meet max size
            if max_size:
                quality = 95  # Start with high quality
                max_size_bytes = parse_size(max_size)
                while True:
                    img_resized.save(output_path, quality=quality)
                    if os.path.getsize(output_path) <= max_size_bytes or quality <= 10:
                        break
                    quality -= 5
            else:
                img_resized.save(output_path)
            
            print(f"Resized: {image_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def parse_size(size_str):
    """Convert size string (e.g., '500KB', '2MB') to bytes."""
    size_str = size_str.upper()
    if size_str.endswith("KB"):
        return int(size_str[:-2]) * 1024
    elif size_str.endswith("MB"):
        return int(size_str[:-2]) * 1024 * 1024
    elif size_str.endswith("GB"):
        return int(size_str[:-2]) * 1024 * 1024 * 1024
    else:
        raise ValueError("Invalid size format. Use KB, MB, or GB (e.g., '500KB', '2MB').")

def resize_images_in_folder(folder_path, percentage, max_width, max_height, max_size):
    # Check for subdirectories
    subdirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    if subdirs:
        raise Exception(f"Error: The folder '{folder_path}' contains subdirectories, which is not supported.")

    output_folder = f"{folder_path}_resized"
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            output_path = os.path.join(output_folder, file_name)
            resize_image(file_path, percentage, max_width, max_height, max_size, output_path)

    print(f"All images resized and saved to: {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images or all images in a folder.")
    parser.add_argument("input_path", help="Path to an image or a folder containing images")
    parser.add_argument("--percentage", type=int, help="Percentage to resize (e.g., 75 for 75%)", default=None)
    parser.add_argument("--max-width", type=int, help="Maximum width for resized images", default=None)
    parser.add_argument("--max-height", type=int, help="Maximum height for resized images", default=None)
    parser.add_argument("--max-size", type=str, help="Maximum file size (e.g., '500KB', '2MB')", default=None)

    args = parser.parse_args()

    if os.path.isfile(args.input_path):  # Input is a single file
        output_path = f"{os.path.splitext(args.input_path)[0]}_resized{os.path.splitext(args.input_path)[1]}"
        resize_image(args.input_path, args.percentage, args.max_width, args.max_height, args.max_size, output_path)
    elif os.path.isdir(args.input_path):  # Input is a folder
        try:
            resize_images_in_folder(args.input_path, args.percentage, args.max_width, args.max_height, args.max_size)
        except Exception as e:
            print(e)
    else:
        print("Invalid input path. Please provide a valid file or folder path.")

