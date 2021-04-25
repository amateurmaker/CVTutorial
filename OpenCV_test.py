import cv2
import numpy as np

# Link: https://www.youtube.com/watch?v=WQeoO7MI0Bs&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

### Chapter 1: importing an image
# name_of_window_str = "Name of Window"
# print("Importing image and putting it in window name: " + name_of_window_str)
#
# img = cv2.imread("resources/face.jpg")
# cv2.imshow(name_of_window_str, img)
# cv2.waitKey(0)

### Chapter 1: Showing a live video from Macbook webcam
# cap = cv2.VideoCapture(0)
#
# # @brief cap.set accepts 2 arguments
# # @param int decides the ID to be changed. ID 3 is height, ID 4 is width, ID 10 is brightness
# # @param int decides the value to be set
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 200)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Name of Video Window", img)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

### Chapter 2: Functions
# img = cv2.imread("resources/face.jpg")
#
# # Grey the Image
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # @brief Blur the Image
# # @param: ksize which is the kernel size. Has to be odd numbers. The larger the number the larger the blur
# # @param: sigmaX
# imgBlur = cv2.GaussianBlur(img, (101, 101), 0, )
# # @brief Blur the Image
# # @param: image
# # @param: Threshold values
# imgCanny = cv2.Canny(img, 101, 101)
# # @brief Blur the Image
# # @param: image
# # @param: kernel is a matrix
# # @param: iterations
# kernel = np.ones((5, 5), np.uint8)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# # @brief Blur the Image
# # @param: image
# # @param: kernel is a matrix
# # @param: iterations
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
#
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Edges Image", imgDialation)
# cv2.imshow("Eroded Image", imgEroded)
#
# cv2.waitKey(0)

### Chapter 3: Resizing and Cropping
img = cv2.imread("resources/face.jpg")
# @brief provides the height, width and channel (BGR is channel 3)
print(img.shape)
# @brief resize the image according to 2 parameters width and height
imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)
cv2.imshow("Resized Image", imgResized)
# @brief resize the image according to 2 parameters height and width
imgCropped = img[1000:3000, 1000:3000]
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)

### Chapter 4: