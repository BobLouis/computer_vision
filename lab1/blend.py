import cv2


def blending(path1, path2):
    image1 = cv2.imread(path1)
    image2 = cv2.imread(path2)

    cv2.imshow("Blend", image1)

    def updateBlend(x):
        # global weight, image1, image2
        weight = cv2.getTrackbarPos("Blend", "Blend") / 255
        image_add = cv2.addWeighted(image1, 1 - weight, image2, weight, 0)
        cv2.imshow("Blend", image_add)

    cv2.createTrackbar("Blend", "Blend", 0, 255, updateBlend)
    cv2.setTrackbarPos("Blend", "Blend", 0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path1 = "strong.png"
    path2 = "weak.png"
    blending(path1, path2)
    