<div align="center">

# Multi-Hough-Circles

</div>

<center>

| ![img1](https://github.com/AydenBravender/Multi-Hough-Circles/blob/main/image1.jpg?raw=true) | ![img2](https://github.com/AydenBravender/Multi-Hough-Circles/blob/main/image2.jpg?raw=true) |
|--------------------------|--------------------------|

</center>

While working with OpenCV's `cv2.HoughCircles`, I noticed that in order to only represent the most accurate cirlces the programmer could change the paremeters or make a function that pulls out the best circle. However neither solution is optimal. The problem with the first is that in one frame a the code is 50% sure about a circle being a circle, and in the next 87% sure. Because of this dynamic behavior you would have to always be adjusting the paraemeters. In the second solution, you only detect the most likely circle. While this works for applications when only one circle is present, once you run into the need to detect multiple circles this solution is no longer useful. In the solution that I am presenting, my code collects user input regarding a 'N' amount of circles that are at max needed to be detected on the screen. It then detects as many circles as it can up to that 'N' amount of circles. You can still use prameters to adjust the lowest certainty you want each circle to have. It judges which identified circles are most likely to be actually circles by comparing the number of keypoints. Overall, this code works great for detecting pretty much any amount of circles including 0. On a Raspberry Pi 4, depending on the amount of circles it needed to detect, it had a range of 37 to 4 frames per second (fps). On a windows laptop it was getting up to 50 frames per second.

