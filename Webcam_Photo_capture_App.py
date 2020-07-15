'''
step1. GoTo Command Prompt and install package opencv using command 'pip install opencv-python'

after running the code
note: image will be saved in the same directory where this python file is located.
image will directly be captured without opening any preview of camera.
'''


import cv2

imgcapture = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = imgcapture.read()
    cv2.imwrite("test.jpg", frame)
    result = False
    print("Image Captured...")

imgcapture.release()