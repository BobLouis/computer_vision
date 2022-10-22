import cv2
import numpy as np


img1_path = 'strong.png'
img2_path = 'weak.png'

def biliter_filter():
    img = cv2.imread(img1_path)
    cv2.imshow("biliter_filter", img)

    def update(x):
        # global weight, img1, img2
        bil_img = cv2.bilateralFilter(img,x,90,90)
        if x == 0:
            cv2.imshow("biliter_filter", img)
        else:
            cv2.imshow("biliter_filter",bil_img)

    cv2.createTrackbar("magnitude:", "biliter_filter", 0, 10, update)
    cv2.setTrackbarPos("magnitude:", "biliter_filter", 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "strong.png"
    path2 = "weak.png"
    biliter_filter()
