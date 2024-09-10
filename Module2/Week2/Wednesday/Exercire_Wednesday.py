import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('D:/Homework/Module2/Week2/Wednesday/1.opencv/image1.png', 1)
plt.imshow(img)
plt.show()
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()
data = np.array([2,3,4])
result = data[::-1]
print(result)