import cv2
import numpy as np
def reziseImageCorrect (img, size):
    pixelValue = int(2**size)
    print(np.mean(img[0::pixelValue, 0::pixelValue]))
    newImage = img[0::pixelValue, 0::pixelValue]
    outputName = 'output_correct' + str(size) + '.png'
    cv2.imwrite(outputName, newImage)

def  reziseImage (img, size):
    newSize = (size, size)
    # resize image
    output = cv2.resize(img, newSize)
    outputName = 'output' + str(size) + '.png'
    cv2.imwrite(outputName,output) 

src = cv2.imread('Imagens/baboon.png', cv2.IMREAD_UNCHANGED)

reziseImage(src, 256)

reziseImage(src, 128)

reziseImage(src, 64)

reziseImage(src, 32)

reziseImage(src, 16)

reziseImage(src, 8)


reziseImageCorrect(src, 1)

reziseImageCorrect(src, 2)

reziseImageCorrect(src, 3)

reziseImageCorrect(src, 4)

reziseImageCorrect(src, 5)

reziseImageCorrect(src, 6)
