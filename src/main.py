import cv2 as cv
import numpy as np
import time

videoCapture = cv.VideoCapture(0)


frame_rate_calc = 1
freq = cv.getTickFrequency()
list1 = []

N = int(input("number of circles: ")) # max amount of circles present on the screen

while True:
    t1 = cv.getTickCount()
    
    ret, frame = videoCapture.read()
    if not ret: break

    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # convert the frame into grayscale
    blurframe = cv.GaussianBlur(grayframe, (17, 17), 0) # blur the grayscale image

    circles = cv.HoughCircles(blurframe, cv.HOUGH_GRADIENT, 1.2, 100, 
                              param1=100, param2=40, minRadius=10, maxRadius=500) # different paremeters to set the base expectations of each circle

    if circles is not None:
        sift = cv.SIFT_create()
        circles = np.uint16(np.around(circles))

        for i in range(len(circles[0])):
            circle = circles[0, i]
            x, y, r = circle

            # Define the region of interest (ROI) around the circle
            roi = frame[y-r:y+r, x-r:x+r]

            # Check if ROI is valid
            if roi.shape[0] > 0 and roi.shape[1] > 0:
                # Detect keypoints and compute descriptors
                keypoints, descriptors = sift.detectAndCompute(roi, None)

                # Get the number of keypoints
                num_keypoints = len(keypoints) 

                list1.append(num_keypoints)
                list1.sort() # arrange the keypoints in order of size
                try:
                    for i in range(N):
                        chosen = circles[0, -(i+1)] # whichever circle has the most keypoints we pick
                        cv.circle(frame, (chosen[0], chosen[1]), 1, (255, 0, 0), 3)
                        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (0, 250, 255), 5)
                except:
                    break


    
    cv.putText(frame, f"FPS: {frame_rate_calc:.2f}", (7, 70), cv.FONT_HERSHEY_SIMPLEX , 1, (100, 255, 0), 2, cv.LINE_AA)
    cv.putText(frame, f"Circles to detect: {N}", (7, 450), cv.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv.LINE_AA)   
    print(f"FPS: {frame_rate_calc:.2f}")

    t2 = cv.getTickCount()
    time1 = (t2-t1)/freq
    frame_rate_calc = 1/time1
    
    cv.imshow('circles', frame)


    if cv.waitKey(1) & 0xFF == ord('q'): 
        cv.imwrite("image2.jpg", frame)

    

videoCapture.release()
cv.destroyAllWindows()












  


