from PIL import Image
import os

def collage(num_images):

    image_size = (400, 400)
    directory = "./static"
    
    if (num_images % 2 == 0):
        num_images_per_row = num_images // 2
        num_images_per_col = num_images // 2

        input_images = []

        # Open the input images
        for i in range(num_images):
            input_images.append(f"storyboardimage{i + 1}.jpg")

        # Open the input images and resize them to the same size (optional)
        images = [Image.open(file).resize((400, 400)) for file in input_images]

        # Create a new image for the collage
        collage_size = (image_size[0] * num_images_per_row, image_size[1] * num_images_per_col)
        collage = Image.new("RGB", collage_size)

        for i in range(num_images_per_row):
            for j in range(num_images_per_col):
                index = i + j * num_images_per_row
                if index < len(images):
                    x = i * image_size[0]
                    y = j * image_size[1]
                    collage.paste(images[index], (x, y))

        # Save the final collage image to a file
        collage.save(os.path.join(directory, "collage.png"))
    else:
        num_images_per_row = (num_images // 2) + 1
        num_images_per_col = num_images // 2

        input_images = []

        # Open the input images
        for i in range(num_images):
            input_images.append(f"storyboardimage{i + 1}.jpg")

        # Open the input images and resize them to the same size (optional)
        images = [Image.open(file).resize((400, 400)) for file in input_images]

        # Create a new image for the collage
        collage_size = (image_size[0] * num_images_per_row, image_size[1] * num_images_per_col)
        collage = Image.new("RGB", collage_size)

        for i in range(num_images_per_row):
            for j in range(num_images_per_col):
                index = i + j * num_images_per_row
                if index < len(images):
                    x = i * image_size[0]
                    y = j * image_size[1]
                    collage.paste(images[index], (x, y))

        # Save the final collage image to a file
        collage.save(os.path.join(directory, "collage.png"))
