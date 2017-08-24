import numpy as np
from PIL import ImageGrab
import cv2

def process_img():
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 500, 540)))
    screen = cv2.resize(screen, (80, 80))
    return screen
