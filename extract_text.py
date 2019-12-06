import pytesseract as ocr
import numpy as np
import cv2

from PIL import Image


def ext_text(path_image):

    # imagem para RGB
    img = Image.open(path_image).convert('RGB')

    # vetor de posições
    array_img = np.asarray(img).astype(np.uint8)

    # Tentatica de redução
    array_img[:, :, 0] = 0 # banda vermelha -> 0
    array_img[:, :, 2] = 0 # banda azul -> 0

    # imagem em escala de cinza
    gray_scale_img = cv2.cvtColor(array_img, cv2.COLOR_RGB2GRAY)

    # limite do valor do pixel
    ret, thresh = cv2.threshold(gray_scale_img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    binary_filter_image = Image.fromarray(thresh)
    binary_filter_image.show()
    text = ocr.image_to_string(binary_filter_image, lang='por')

    print(text)
    return text
