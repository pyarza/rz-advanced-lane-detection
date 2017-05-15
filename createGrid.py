import numpy as np
import cv2

# Based on;
# http://stackoverflow.com/questions/2169478/how-to-make-a-checkerboard-in-numpy

w, h = 720, 1280
sq = 40
color1 = (0xFF, 0x80, 0x00)
color2 = (0x80, 0xFF, 0x00)


def use_ogrid():
    coords = np.ogrid[0:w, 0:h]
    idx = (coords[0] // sq + coords[1] // sq) % 2
    vals = np.array([color1, color2], dtype=np.uint8)
    img = vals[idx]
    return img


if __name__ == '__main__':
    img = use_ogrid()
    write_name = 'grid' + str(sq) + '.jpg'
    cv2.imwrite(write_name, img)
