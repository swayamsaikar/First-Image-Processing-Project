import cv2
import numpy as np

CameraObj = cv2.VideoCapture(0)
MyImage = cv2.imread("MyImage.jpg")

while(True):
    ret, frame = CameraObj.read()

    print(frame)  # it will give a multi-dimensional array

    # now we have to resize the frame and myImage to the same size
    frame = cv2.resize(frame, (640, 480))
    MyImage = cv2.resize(MyImage, (640, 480))

    # code to pass the faint shade value and dark shade value of RBG.
    # this code is to locate , from which part of the image to which part of the image you want to perform the operation
    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    # this cv2.inRange() checks and returns the part of the array which lies in the between of the above two arrays
    # !!!! You can read More about this function Here :- https://www.educba.com/opencv-inrange/
    maskedImage = cv2.inRange(frame, u_black, l_black)

    # prints the masked image in the form of multi-dimensional array
    print(maskedImage)

    # now we will merge frame and mask to make a new image
    # return : if both the comparing bits are 1, then the Bitwise AND will return 1 otherwise 0
    # !!!! Learn More : https://www.educba.com/python-bitwise-operator/
    result = cv2.bitwise_and(frame, frame, mask=maskedImage)

    # then we will cut out the masked image from the page and we wil leftout with the background
    f = frame - result
    # np.where is like if else
    f = np.where(f == 0, MyImage, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

CameraObj.release()
cv2.destroyAllWindows()
