import os
import glob
from PIL import Image

def create_gif_from_directory(folder_path, output_gif_path, duration_ms=100):
    """
    Creates an animated GIF from all images in a specified folder.

    :param folder_path: Path to the directory containing the images.
    :param output_gif_path: Filename for the output GIF (e.g., 'output.gif').
    :param duration_ms: Duration each frame is displayed, in milliseconds (default is 100ms).
    """
    # 1. Get a list of all image file paths
    # glob.glob finds all files matching a pattern. Sorting ensures correct order.
    # Adjust the pattern (e.g., '*.png') to match your image file types.
    image_paths = sorted(glob.glob(os.path.join(folder_path, '*.png')))
    
    if not image_paths:
        print(f"No images found in {folder_path} matching '*.png'")
        return

    # 2. Load the images
    images = []
    for file_path in image_paths:
        try:
            img = Image.open(file_path).convert('RGB')
            images.append(img)
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")

    if not images:
        print("Could not load any images.")
        return

    # 3. Create and save the GIF
    # The first image is used as the base, and remaining frames are appended.
    first_frame = images[0]
    first_frame.save(
        output_gif_path,
        save_all=True,
        append_images=images[1:], # Append all frames except the first one
        duration=duration_ms,
        loop=0 # 0 means the GIF will loop infinitely
    )
    
    print(f"GIF successfully created and saved at: **{output_gif_path}**")

# --- Example Usage ---
# Make sure your directory and images exist!
image_directory = 'imgs' # <-- CHANGE THIS
output_filename = 'my_animation.gif' 
frame_duration = 42 # 200 milliseconds (5 frames per second)

create_gif_from_directory(image_directory, output_filename, duration_ms=frame_duration)
