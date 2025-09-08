from PIL import Image

# Create a 1x1 white pixel
img = Image.new("RGB", (1, 1), (255, 255, 255))
img.save("pixel.jpg")
