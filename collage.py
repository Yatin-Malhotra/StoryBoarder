from PIL import Image

def collage(num_images):
    # Open the input images
    input_images = []

    for i in range(num_images):
        input_images.append(f"storyboardimage{i + 1}.jpg")

    # Open the input images and resize them to the same size (optional)
    images = [Image.open(file).resize((400, 400)) for file in input_images]

    # Create a new image with the desired size and mode (RGB or RGBA)
    collage_width = num_images * images[0].width
    collage_height = images[0].height
    collage_mode = "RGB"
    collage_image = Image.new(collage_mode, (collage_width, collage_height))

    # Paste the input images into the collage image
    for i, image in enumerate(images):
        x_offset = i * image.width
        collage_image.paste(image, (x_offset, 0))
        # Save the collage image with a name based on the counter
        collage_image.save(f"collage_{i+1}.jpg")

    # Save the final collage image to a file
    collage_image.save("collage.jpg")
