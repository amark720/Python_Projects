'''

minimize the ScreenRecorder popup window that opens after running the program so that it can capture the screen without
giving any multiple window popups recording.

'''

import cv2
import numpy as np
from PIL import ImageGrab
import time

def screenRecorder():
    time.sleep(5)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))
    # Here 5.0 is the frame rate and 1366,768 is the screen size

    while (1):
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", frame)
        out.write(frame)

        if cv2.waitKey(1) ==27:
            break
    out.release()
    cv2.destroyAllWindows()
screenRecorder()
