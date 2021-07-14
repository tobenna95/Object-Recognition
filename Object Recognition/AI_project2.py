import cv2
import matplotlib.pyplot as plt
import numpy as np

# path of the image to read.
path = r"/Users/tobennaeze/Downloads/Images/image-3.bmp"

# Read image in black and white or grayscale format
img = cv2.imread(path,0)


# Grayscale histogram
gray_hist = cv2.calcHist([img_grayscale], [0], None, [256], [0,256] )
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Resizing image
resize = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resize)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian Blur', gauss)

# Edge Detection Canny
canny = cv2.Canny(gauss, 125, 175, apertureSize=3)
cv2.imshow('Canny Edges', canny)

# Hough Transform
lines = cv2.HoughLines(canny, 1, np.pi*3/4, 100)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho 
    x1 = int (x0 + 1000 *(-b))
    y1 = int (y0 + 1000 * (a))
    x2 = int (x0 - 1000 *(-b))
    y2 = int (y0 - 1000 * (a))
    cv2.line(canny, (x1, y1), (x2, y2), (255, 0, 0), 2)

#Display the image
cv2.imshow('image', canny)




cv2.waitKey(0)
cv2.destroyAllWindows()
