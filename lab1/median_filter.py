import cv2
import numpy as np


img1_path = 'strong.png'
img2_path = 'weak.png'

def median_filter():
    img = cv2.imread(img1_path)
    cv2.imshow("median_filter", img)

    def update(x):
        # global weight, img1, img2
        k = 2*x+1
        med_img = cv2.medianBlur(img,k)
        if x == 0:
            cv2.imshow("median_filter", img)
        else:
            cv2.imshow("median_filter",med_img)

    cv2.createTrackbar("magnitude:", "median_filter", 0, 10, update)
    cv2.setTrackbarPos("magnitude:", "median_filter", 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "strong.png"
    path2 = "weak.png"
    median_filter()
