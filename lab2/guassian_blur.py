import cv2
import numpy as np


img1_path = 'building.png'


def gaussian_blur():
    img = cv2.imread(img1_path)
    img_gray = np.zeros(img.shape[:2], dtype=np.uint8)
    img_blur = np.zeros(img.shape[:2], dtype=np.uint8)
    print(img_gray.shape)
    print(img[0,0])
    for i in range(img_gray.shape[0]):
        for j in range(img_gray.shape[1]):
            img_gray[i,j] = int(np.dot(img[i,j], [0.114,0.587,0.299]))

    for i in range(1,img_gray.shape[0]-1):
        for j in range(1,img_gray.shape[1]-1):
            # section = np.array([img_gray[i-1,j-1],img_gray[i,j-1],img_gray[i+1,j-1]], \
            #                   [img_gray[i - 1, j], img_gray[i, j ], img_gray[i + 1, j ]], \
            #                   [img_gray[i - 1, j + 1], img_gray[i, j + 1], img_gray[i + 1, j + 1]])
            # kernel = np.array([0.045,0.122])
            img_blur[i,j] = int(img_gray[i-1,j-1] * 0.045 + img_gray[i,j-1] * 0.122 + img_gray[i+1,j-1] * 0.045+\
                            img_gray[i - 1, j] * 0.122+ img_gray[i, j] * 0.332 + img_gray[i + 1, j] * 0.122+ \
                            img_gray[i - 1, j + 1] * 0.045 + img_gray[i, j + 1] * 0.122 + img_gray[i + 1, j + 1] * 0.045)




    cv2.imshow("gray",img_gray)
    cv2.imshow("blur", img_blur)
    cv2.waitKey(0)





if __name__ == "__main__":
    gaussian_blur()
