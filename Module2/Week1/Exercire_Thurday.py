import numpy as np

boxA = [0, 0, 100, 100]
boxB = [50, 50, 150, 150]

def compute_IOU(boxA, boxB):
    # Xac dinh toa do cua intesection
    it_xA = max(boxA[0], boxB[0])
    it_yA = max(boxA[1], boxB[1])
    it_xB = min(boxA[2], boxB[2])
    it_yB = min(boxA[3], boxB[3])
    # tinh dien tich intersection
    it_ares = max(0, it_xB-it_xA + 1)*max(0, it_yB-it_yA + 1)
    # tinh dien tich boxA, boxB
    boxA_ares = (boxA[2] - boxA[0] + 1)*(boxA[3] - boxA[1] + 1)
    boxB_ares = (boxB[2] - boxB[0] + 1)*(boxB[3] - boxB[1] + 1)
    # tinh iou

    iou = it_ares/(boxA_ares + boxB_ares - it_ares)

    return iou


boxes = np.array([
    [12, 84, 140, 212],
    [24, 84, 152, 212],
    [36, 84, 164, 212],
    [12, 96, 140, 224],
    [24, 96, 152, 224],
])
scores = np.array([0.3, 0.4, 0.5, 0.6, 0.7])
def compute_IOU_np(boxes, scores, IOU_threshold):
    # xac dinh cac vector
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    # non_maxium

    order = scores.argsort()[::-1]
    print(order[0])
    keep = []
    while order.size > 0:
        keep.append(boxes[order[0]])
        # so sanh va lay toa do cua intersection cua cac box tu vij tri thu 1 tro ve cuoi
        maxX1 = np.maximum(x1[0], x1[1::])
        maxY1 = np.maximum(y1[0], y1[1::])
        minX2 = np.minimum(x2[0], x2[1::])
        minY2 = np.minimum(y2[0], y2[1::])
        # tinh intersection arena
        it_arena = np.maximum(0, (minX2-maxX1 +1))*np.maximum(0, (minY2 - maxY1 +1))
        # tinh box0, boxi arena
        box0_arena = (x2[0]-x1[0] + 1)*(y2[0]- y1[0] + 1)
        boxi_arena = (x2[1::]-x1[1::] + 1)*(y2[1::]- y1[1::] + 1)
        # IOU
        IOU_arr = it_arena/(box0_arena + boxi_arena - it_arena)


