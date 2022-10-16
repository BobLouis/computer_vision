import cv2
import numpy as np


img1_path = 'strong.png'
img2_path = 'weak.png'

def gaussian_blur():
    img = cv2.imread(img1_path)


    cv2.imshow("guassian_blur", img)

    def update(x):
        # global weight, img1, img2
        k = 2*x+1
        gau_img = cv2.GaussianBlur(img,(k,k),0)
        if x == 0:
            cv2.imshow("guassian_blur", img)
        else:
            cv2.imshow("guassian_blur",gau_img)

    cv2.createTrackbar("magnitude:", "guassian_blur", 0, 10, update)
    cv2.setTrackbarPos("magnitude:", "guassian_blur", 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "strong.png"
    path2 = "weak.png"
    gaussian_blur()
