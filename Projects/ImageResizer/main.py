import cv2

# Configurable Parameter
source = "kitten.png"
destination = "newImage.png"
scale_percent = 50 # percent by which the image is resized

src = cv2.imread(source, cv2.IMREAD_UNCHANGED) # To load image
# cv2.imshow("title", src) -> will show the img

# Calculate the 50% of original dimensions
new_width = int(src.shape[1] * scale_percent / 100) # original img ka 50% width
new_height = int(src.shape[0] * scale_percent / 100) # original img ka 50% height

# dsize
dsize = (new_width, new_height) # tuple

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output) # will create a new image from the output
# cv2.waitKey(0)