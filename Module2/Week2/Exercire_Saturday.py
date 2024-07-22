# import thưu viện
import numpy as np
import cv2
import matplotlib.pyplot as plt

# read image and transform to gray style
img = cv2.imread('D:/Homework/Module2/Week2/Wednesday/4.convert_color/image_color.png', 0)
plt.imshow(img)
plt.show()
# take size and chose the transformation

height, width = img.shape
a = np.array([[1,0],
             [0,-1]])

p = np.array([0, height - 1])

# transformation
out_put = np.zeros((height, width))
for x2 in range(height):
    for x1 in range(width):
        color_img = img[x2,x1]
        v = np.array([x1,x2])
        x1_new, x2_new = a.dot(v) + p
        out_put[x2_new, x1_new] = color_img

plt.imshow(out_put)
plt.show()

#import library
import numpy as np
import matplotlib.pyplot as plt
import cv2

# read the picture

img = cv2.imread('D:/Homework/Module2/Week2/Wednesday/4.convert_color/image_color.png', 0)
height, width = img.shape
plt.imshow(img)
plt.show()

# take the transformation

a = np.array([[-1, 0],
              [0, 1]])
p = np.array([width - 1, 0])
output = np.zeros((height, width))
# transformation

for x2 in range(height):
    for x1 in range(width):
        color_img = img[x2,x1]
        v = np.array([x1,x2])
        x1_new, x2_new = a.dot(v)+p
        output[x2_new, x1_new] = color_img

plt.imshow(output)
plt.show()



#import library
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('D:/Homework/Module2/Week2/Wednesday/4.convert_color/image_color.png', 0)
height, width = img.shape
coords = np.indices((height, width)).reshape(2, -1)
print(coords)
coords = np.vstack((coords[1], coords[0]))
plt.imshow(img)
plt.show()
img_resize = np.reshape(img, (2, -1), 'C')
# take the transformation

a = np.array([[1, 0],
              [0, -1]])
import numpy as np
p = np.array([0, height - 1]).reshape(2,1)
print(p)
# transformation

out_put = a.dot(img_resize) + p
out_put = np.reshape(out_put, (height, width), 'C')
plt.imshow(out_put)
plt.show()
