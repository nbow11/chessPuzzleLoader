from PIL import Image
import os

# define input and output directories
input_dir = "chessImageData/blank2/"
output_dir = "chessImageData/blank/"

# create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# loop through all files in the input directory
for filename in os.listdir(input_dir):
    # open the image file
    with Image.open(os.path.join(input_dir, filename)).convert("RGB") as img:
        # crop or resize the image to make it a square of size 85x85
        width, height = img.size
        if width != height:
            # crop the image to a square
            min_dim = min(width, height)
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            img = img.crop((left, top, right, bottom))
        img = img.resize((85, 85))

        # save the processed image to the output directory
        img.save(os.path.join(output_dir, filename))