<div align="center">

# Multi-Hough-Circles

</div>
<center>

| ![img1](https://github.com/AydenBravender/Multi-Hough-Circles/blob/main/image1.jpg?raw=true) | ![img2](https://github.com/AydenBravender/mediapipe_door_opener/blob/main/dooropening.gif?raw=true) |
|--------------------------|--------------------------|

</center>

While working with OpenCV's ```cv2.HoughCircles``` I found that when you are trying to find more than one circle in a frame, it struggled. It would either detect only one, or you would have to change your confidence rate, leading to lots of circles all over your window. My code collects user input regarding the max amount of circles detected in the screen, and then detects that number of circles with the highest keypoints. Overall this code works great for detecting pretty much any amount of circles including 0. On a Raspberry pi 4, depending on the amount of circles it needed to detect, it had a range of fps from 37 to 4.
