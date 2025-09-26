# با مقادیر مثبت 8 بیتی نمایش دهید (0 تا 255)
import cv2
import matplotlib.pyplot as plt

image_path = './Input_Images/DarkImage.jpg'

# read image to grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# normalize
image_8bit = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

# save image
cv2.imwrite('DarkImage_8bit.jpg', image_8bit)

#show output
plt.imshow(image_8bit, cmap='gray')
plt.axis('off')
plt.show()




