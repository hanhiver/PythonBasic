import cv2 
import numpy as np
from PIL import Image

cv2_img = cv2.imread('dog.jpg')

cv2_img[:, :, [0, 2]] = cv2_img[:, :, [2, 0]]

pil_img = Image.fromarray(cv2_img)

pil_img.show()


