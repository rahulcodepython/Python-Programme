# We use qrcode module version 7.3.1
# We use pillow module version 9.0.1

import qrcode

img = qrcode.make("Hi I am good.") #That is a demo text

img.save("image.png") #The name of the image 