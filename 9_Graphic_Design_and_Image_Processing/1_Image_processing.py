from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 1)Display an Image
img = Image.open("rubangino.png")
# img.show()
# print("Image opened successfully")

# 2)Plot the image in console window
plt.imshow(mpimg.imread('rubangino.png'))
plt.show()

# 3)Display the image size(width and height)
w, h = img.size
# print("Width: ", w, end="   ")
# print("Height: ", h)

# 4)Reduce the Image size of its half size
resized_img = img.resize((round(img.size[0] * 0.5), round(img.size[1] * 0.5)))
resized_img.save('resizedImg.png')
w, h = resized_img.size
# print("Resized width: ", w, end="   ")
# print("Resized height: ", h)
# resized_img.show()

# 5) Rotate the image 145 degrees
angle = 145
rotatedImg = img.rotate(angle)
rotatedImg.save('rotatedImg.png')
# rotatedImg.show()

# 6) Resize the image with 50units in x direction and 70  units in y direction
customResize = img.resize((50, 70))
customResize.save('customResize.png')
# customResize.show()

# 7) Flip the image (Left to Right, Top to Bottom)
flippedToLeft = img.transpose(Image.FLIP_LEFT_RIGHT)
flippedToLeft.save('leftRightFlipeed.png')
# flippedToLeft.show()

flippedToTop = img.transpose(Image.FLIP_TOP_BOTTOM)
flippedToTop.save('topBottomFlipped.png')
flippedToTop.show()

# 8) Crop the image
croppedImg = img.crop((1, 2, 300, 300))
croppedImg.save('croppedImage.png')
# croppedImg.show()

# 9) Change the color of the image to Gray Scale, Black and Wihte
changeGrey = img.convert('LA')
changeGrey.save('greyImg.png')
# changeGrey.show()
changeBW = img.convert('L')
changeBW.save('bwImg.png')
# changeBW.show()

# 10) Apply blur effect to the image
blurImage = img.filter(ImageFilter.GaussianBlur(10))
blurImage.save('blurredImg.png')
blurImage.show()

