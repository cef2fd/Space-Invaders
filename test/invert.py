from PIL import Image
import PIL.ImageOps

image = Image.open('ship2.bmp')

inverted_image = PIL.ImageOps.invert(image)

inversted_image.save('images/ship_invert.bmp')