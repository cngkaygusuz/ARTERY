import cv2 as cv
import numpy as np


HEIGHT = 600
WIDTH = 960

NPDIM = (HEIGHT, WIDTH)
CVDIM = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)

NUM_LINES = 20

GAUSSIAN_KERNEL_SIZE = 3
GAUSSIAN_KERNEL = (GAUSSIAN_KERNEL_SIZE, GAUSSIAN_KERNEL_SIZE)


def show(img):
    cv.imshow('img', img)
    cv.waitKey(0)


def main():
    # initiate empty canvas
    img = np.zeros(NPDIM, np.uint8)

    for i in range(NUM_LINES+1):
        cv.line(img, (0, 0), (WIDTH, i*(HEIGHT//NUM_LINES)), WHITE, lineType=cv.LINE_AA)

        cv.line(img, CVDIM, (0, i*(HEIGHT//NUM_LINES)), WHITE, lineType=cv.LINE_AA)

        cv.line(img, (0, HEIGHT), (WIDTH, i*(HEIGHT//NUM_LINES)), WHITE, lineType=cv.LINE_AA)

        cv.line(img, (WIDTH, 0), (0, i*(HEIGHT//NUM_LINES)), WHITE, lineType=cv.LINE_AA)

    img = cv.GaussianBlur(img, GAUSSIAN_KERNEL, 0)

    show(img)


if __name__ == '__main__':
    main()
