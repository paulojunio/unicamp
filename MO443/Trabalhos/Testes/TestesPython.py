from PIL import Image
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

plt.gray()

im1 = Image.open('Imagens/baboon.png')  
plt.imshow(im1)
plt.imsave('iris1.png', im1)
plt.show()
# open image file and stores it in a numpy array
img = np.array(Image.open('Imagens/baboon.png'), 'f')
# print image dimensions and type
print (img.shape, img.dtype)
print(img)

# save image in PNG format
plt.imsave('iris.png', img)
# calculate some statistical information
print (img.min(), img.mean(), img.max())
# apply rotation transformation
f = np.flipud(img)
plt.imshow(f)
plt.imsave('iris1.png', f)
plt.show()
# smooth image with Gaussian filter
g = ndimage.gaussian_filter(img, sigma=7)
h = ndimage.gaussian_filter(img, sigma=11)
plt.imshow(g)
plt.imsave('iris2.png', g)
plt.show()
plt.imshow(h)
plt.imsave('iris3.png', h)
plt.show()
