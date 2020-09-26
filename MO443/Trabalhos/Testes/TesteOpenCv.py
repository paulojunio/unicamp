import cv2

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