import cv2 

from objDetection import obj

def image():
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)
	while True:
		try:
			check, frame = webcam.read()
			cv2.imshow("Capturing", frame)
			key = cv2.waitKey(1)
			if key == ord('s'): 
				cv2.imwrite(filename='saved_img.jpg', img=frame)
				webcam.release()
				img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
				#img_new = cv2.imshow("Captured Image", img_new)
				cv2.waitKey(1650)
				cv2.destroyAllWindows()
				break
				
			elif key == ord('q'):
			    print("Turning off camera.")
			    webcam.release()
			    print("Camera off.")
			    print("Program ended.")
			    cv2.destroyAllWindows()
			    break
			
		except(KeyboardInterrupt):
			print("Turning off camera.")
			webcam.release()
			print("Camera off.")
			print("Program ended.")
			cv2.destroyAllWindows()
			break

	return(obj('/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/saved_img.jpg'))

