import cv2  
import numpy as np

#trackbar callback fucntion does nothing but required for trackbar



def nothing(x):
	pass 

def change_color(x):
	#condition to change color if trackbar value is greater than 127 
	if(cv2.getTrackbarPos('r','controls')>127):
		global color
		color=(255,0,0)
	else:
		color=(0,0,255)

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')
#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('r','controls',15,255,change_color)
cv2.createTrackbar('s','controls',0,1,nothing)

#initial color
color=(0,0,255)


while(1):
	#create a black image 
	img = np.zeros((512,512,3), np.uint8)
	#calculate center of image
	img_center_y=img.shape[0]//2
	img_center_x=img.shape[1]//2



	#returns current position/value of trackbar 
	radius= int(cv2.getTrackbarPos('r','controls'))
	#returns current slider value of trackbar 's'
	shape=cv2.getTrackbarPos('s','controls')

	#checks if shape varible is off (0) or on (1)
	#draw square if switch is on
	if(shape==1): 
		start_point=(img_center_y-100,img_center_x-100)
		end_point=(img_center_y+100,img_center_x+100)
		#change thickness of square based in trackbar 'r'
		thickness = radius
		#create a square
		image = cv2.rectangle(img, start_point, end_point, color, thickness) 
		pass
	#draw circle if switch is off
	else:
		#draw a red circle 
		cv2.circle(img,(img_center_y,img_center_x), radius, color, -1)
	#show the image window
	cv2.imshow('img',img)
	
	#waitfor the user to press escape and break the while loop 
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
		
#destroys all window
cv2.destroyAllWindows()
