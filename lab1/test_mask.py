import numpy as np
import cv2
 
# 在画布中心画了一个250*250像素的矩形，用白色填充
# 注意：这是一个二维矩阵，反映在图片上是单通道的
rectangle = np.zeros((300, 300), dtype="uint8")
print(rectangle.shape)
# 第二个参数为矩形左上角的点的坐标，第三个参数为矩形右下角的点的坐标
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
print(rectangle.shape)
cv2.imshow("Rectangle", rectangle)
 
# # 在画布中心画了一个半径150像素的圆圈，用白色填充
# # 注意：这是一个二维矩阵，反映在图片上是单通道的
# circle = np.zeros((300, 300), dtype="uint8")
# cv2.circle(circle, (150, 150), 150, 255, -1)
# cv2.imshow("Circle", circle)
 
# mask为矩形，用白色填充
# dtype="uint8"要写上，保持一致
# 注意：mask维数需要与被mask作用的图片高与宽的维数一致，如下两句话一样的
# mask = np.zeros((300, 300), dtype="uint8")            # mask的高与宽=原图的高与宽
mask = np.zeros(rectangle.shape[:2], dtype="uint8")     # mask的高与宽=原图的高与宽
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)
 
# # 按位与操作AND
# bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow("AND", bitwiseAnd)
# # 先按位与操作AND，再进行mask操作
# bitwiseAndMask = cv2.bitwise_and(rectangle, circle, mask=mask)
# cv2.imshow("bitwiseAndMask", bitwiseAndMask)
 
# # 按位或操作OR
# bitwiseOr = cv2.bitwise_or(rectangle, circle)
# cv2.imshow("OR", bitwiseOr)
# # 先按位或操作OR，再进行mask操作
# bitwiseOrMask = cv2.bitwise_or(rectangle, circle, mask=mask)
# cv2.imshow("bitwiseOrMask", bitwiseOrMask)
 
# # 按位异或XOR
# bitwiseXor = cv2.bitwise_xor(rectangle, circle)
# cv2.imshow("XOR", bitwiseXor)
 
# # 按位非NOT
# bitwiseNot = cv2.bitwise_not(circle)
# cv2.imshow("NOT", bitwiseNot)
 
cv2.waitKey(0)  # 等待用户输入，按任意键即可
