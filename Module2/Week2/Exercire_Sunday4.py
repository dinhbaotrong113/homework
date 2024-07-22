# import library
import numpy as np
import cv2
import matplotlib.pyplot as plt

bg1_imge = cv2.imread("D:/Homework/Module2/Week2/Exercise04_Data/Object.png", 1)
ob_imge = cv2.imread("D:/Homework/Module2/Week2/Exercise04_Data/Object.png", 1)
bg2_imge = cv2.imread("D:/Homework/Module2/Week2/Exercise04_Data/NewBackground.jpg", 1)
templet = cv2.imread("D:/Homework/Module2/Week2/Exercise04_Data/GreenBackground.png",1)

plt.imshow(bg2_imge)
plt.show()
image_size = (678, 381)
bg1_imge = cv2.resize(bg1_imge, image_size)
ob_imge = cv2.resize(ob_imge, image_size)
bg2_imge = cv2.resize(bg2_imge, image_size)
templet = cv2.resize(templet, image_size)


sub_bg1 = cv2.absdiff(bg1_imge, templet)
sub_bg1 = (np.sum(sub_bg1, axis=2)/3)
sub_bg1 = sub_bg1.astype("uint8")
sub_bg1 = np.where(sub_bg1 >= 5, 255, 0)
bg2_imge[np.where(sub_bg1 == 255)] = ob_imge[np.where(sub_bg1 == 255)]
plt.imshow(bg2_imge)
plt.show()
