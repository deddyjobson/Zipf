from numpy import *
try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import image_to_string

img = Image.open('eng.jpg')
story = image_to_string(img, lang = 'eng')

print story