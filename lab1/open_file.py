import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel,QPushButton
from PyQt5.QtGui import (QIcon,QFont)
import cv2
import numpy as np
img1 = 'strong.png'
img2 = 'weak.png'
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '2022 Opencvdl Hw1'
        self.left = 10
        self.top = 10
        self.width = 1040
        self.height = 480
        self.file1 = 'No image loaded                                   '
        self.file2 = 'No image loaded                                   '
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #file load 
        self.file_label1 = QLabel(self.file1, self)
        self.file_label1.move(40, 150)
        self.file_label1.setFont(QFont('Arial', 18))
        self.file_buttton1 = QPushButton('Load image 1', self)
        self.file_buttton1.move(40, 120)
        self.file_buttton1.clicked.connect(self.openFileNameDialog1)
        
        self.file_label2 = QLabel(self.file1, self)
        self.file_label2.move(40, 350)
        self.file_label2.setFont(QFont('Arial', 18))
        self.file_buttton2 = QPushButton('Load image 2', self)
        self.file_buttton2.move(40, 320)
        self.file_buttton2.clicked.connect(self.openFileNameDialog2)

        #image processing============================================================
        self.image_process_label = QLabel('1.image Processing', self)
        self.image_process_label.move(340, 50)
        self.image_process_label.setFont(QFont('Arial', 18))
        
        self.img_proc_button1 = QPushButton('Color Seperation', self)
        self.img_proc_button1.move(340, 120)
        self.img_proc_button1.clicked.connect(self.img_proc_func1)
        
        self.img_proc_button2 = QPushButton('Color Transformation', self)
        self.img_proc_button2.move(340, 200)
        self.img_proc_button2.clicked.connect(self.img_proc_func2)
        
        self.img_proc_button3 = QPushButton('Color Detection', self)
        self.img_proc_button3.move(340, 280)
        self.img_proc_button3.clicked.connect(self.img_proc_func3)
        
        self.img_proc_button4 = QPushButton('Blending', self)
        self.img_proc_button4.move(340, 350)
        self.img_proc_button4.clicked.connect(self.img_proc_func4)
        
        
        
        # image smoothing============================================================
        self.image_smoothing_label = QLabel('2.image Smoothing', self)
        self.image_smoothing_label.move(740, 50)
        self.image_smoothing_label.setFont(QFont('Arial', 18))
        
        self.img_smo_button1 = QPushButton('Gaussian Blur', self)
        self.img_smo_button1.move(740, 120)
        self.img_smo_button1.clicked.connect(self.openFileNameDialog1)
        
        self.img_smo_button2 = QPushButton('Bilateral filter', self)
        self.img_smo_button2.move(740, 200)
        self.img_smo_button2.clicked.connect(self.openFileNameDialog1)
        
        self.img_smo_button3 = QPushButton('Median filter', self)
        self.img_smo_button3.move(740, 280)
        self.img_smo_button3.clicked.connect(self.openFileNameDialog1)
        self.show()

    def openFileNameDialog1(self):    
        global img1
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file1, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.file1:
            print(self.file1)
        img1 = self.file1
        self.file_label1.setText(self.file1.split('/')[-1])
        
    def openFileNameDialog2(self):    
        global img2
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file2, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.file2:
            print(self.file2)
        img2 = self.file2  
        self.file_label2.setText(self.file2.split('/')[-1])
        
    def img_proc_func1(self):
        img = cv2.imread(img1)            #opencv读取图像文件
        (B, G, R) = cv2.split(img) # 3 channel
            
        # make all zeros channel
        zeros = np.zeros(img.shape[:2], dtype = np.uint8)
        print(img.shape[:2])

        b_merge = cv2.merge([B,zeros,zeros])
        g_merge = cv2.merge([zeros,G,zeros])
        r_merge = cv2.merge([zeros,zeros,R])



        cv2.imshow('image',img)
        cv2.imshow("Blue", b_merge)
        cv2.imshow("Green", g_merge)
        cv2.imshow("Red", r_merge)

        # cv2.imshow("merged 1", merged)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        
    def img_proc_func2(self):
        img = cv2.imread(img1)
        (B, G, R) = cv2.split(img) # 3 channel        
        # make all zeros channel
        zeros = np.zeros(img.shape[:2], dtype = np.uint8)
        # print(img.shape[:2])

        b_merge = cv2.merge([B,zeros,zeros])
        g_merge = cv2.merge([zeros,G,zeros])
        r_merge = cv2.merge([zeros,zeros,R])
        averge_value = np.divide((B+G+R),3)
        # print(B.shape)
        averge_value = averge_value.astype(np.uint8)
        b_averge = cv2.merge([averge_value,zeros,zeros])
        g_averge = cv2.merge([zeros,averge_value,zeros])
        r_averge = cv2.merge([zeros,zeros,averge_value])

        b_gray = cv2.cvtColor(b_merge, cv2.COLOR_BGR2GRAY)
        g_gray = cv2.cvtColor(g_merge, cv2.COLOR_BGR2GRAY)
        r_gray = cv2.cvtColor(r_merge, cv2.COLOR_BGR2GRAY)
        mix = b_gray+g_gray+r_gray
        averge_mix = b_averge+g_averge+r_averge

                    
        cv2.imshow('cv2 function',mix)
        cv2.imshow('averge weighted',averge_mix)

        cv2.waitKey(0) 
        cv2.destroyAllWindows()     
        
    def img_proc_func3(self):
        
        img = cv2.imread(img1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_green = np.array([35, 43, 46])
        upper_green = np.array([77, 255, 255])
        green_mask_sing = cv2.inRange(hsv, lower_green, upper_green)
        green_mask = np.zeros_like(img)
        green_mask[:,:,0] = green_mask_sing
        green_mask[:,:,1] = green_mask_sing
        green_mask[:,:,2] = green_mask_sing
        green = cv2.bitwise_and(green_mask, img)

        sensitivity = 15
        lower_white = np.array([0,0,255-sensitivity])
        upper_white = np.array([255,sensitivity,255])
        white_mask_sing = cv2.inRange(hsv, lower_white, upper_white)
        white_mask = np.zeros_like(img)
        white_mask[:,:,0] = white_mask_sing
        white_mask[:,:,1] = white_mask_sing
        white_mask[:,:,2] = white_mask_sing
        white = cv2.bitwise_and(white_mask, img)

        cv2.imshow("image", img)
        cv2.imshow("green mask", green_mask)
        cv2.imshow("white mask", white_mask)
        cv2.imshow("green", green)
        cv2.imshow("white", white)

        cv2.waitKey(0)
        cv2.destroyAllWindows()     
        
        
    def img_proc_func4(self):
        print("func4")
                
        
            
 

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())


img = cv2.imread(img1)
cv2.imshow('oxxostudio', img)

contrast = 0    # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值
cv2.imshow('oxxostudio', img)

# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c/100 + 1) - c + b    # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    cv2.imshow('oxxostudio', output)

# 定義調整亮度函式
def brightness_fn(val):
    global img, contrast, brightness
    brightness = val - 100
    adjust(img, contrast, brightness)

# 定義調整對比度函式
def contrast_fn(val):
    global img, contrast, brightness
    contrast = val - 100
    adjust(img, contrast, brightness)

cv2.createTrackbar('brightness', 'oxxostudio', 0, 200, brightness_fn)  # 加入亮度調整滑桿
cv2.setTrackbarPos('brightness', 'oxxostudio', 100)
cv2.createTrackbar('contrast', 'oxxostudio', 0, 200, contrast_fn)      # 加入對比度調整滑桿
cv2.setTrackbarPos('contrast', 'oxxostudio', 100)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()