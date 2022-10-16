import cv2
import numpy as np

def blending(path1, path2):
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    # cv2.imshow("Blend", img1)
    print(img1.shape[:2])
    img2 = cv2.resize(img2, (img1.shape[1],img1.shape[0]), interpolation=cv2.INTER_AREA)
    print(img1.shape)
    print(img2.shape)
    white = np.full(img1.shape, 255, type(img1[0, 0, 0]))
    combine = np.concatenate((img1, white), axis=1)


    cv2.imshow('Blend', combine)

    def updateBlend(x):
        # global weight, img1, img2
        zero = np.full(img1.shape,255,type(img1[0,0,0]))
        weight = cv2.getTrackbarPos("Blend", "Blend") / 255
        image_add1 = cv2.addWeighted(img1, 1 - weight, zero, weight, 0)
        image_add2 = cv2.addWeighted(zero, 1 - weight, img2, weight, 0)
        combine = np.concatenate((image_add1, image_add2), axis=1)
        cv2.imshow("Blend", combine)

    cv2.createTrackbar("Blend", "Blend", 0, 255, updateBlend)
    cv2.setTrackbarPos("Blend", "Blend", 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "strong.png"
    path2 = "weak.png"
    blending(path1, path2)
