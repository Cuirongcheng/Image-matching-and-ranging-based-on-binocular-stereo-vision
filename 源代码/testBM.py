import numpy as np
import cv2
import camera_configs\


# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(threeD[y][x])

cv2.setMouseCallback("depth", callbackFunc, None)

while True:

    # 打开左右图像
    img1 = cv2.imread("./img/01.bmp")
    img2 = cv2.imread("./img/02.bmp")
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(img1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(img2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)
    cv2.imshow("rect1", img1_rectified)
    cv2.imshow("rect2", img2_rectified)

    # 将图片置为灰度图，为StereoBM作准备
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray1", imgL)
    cv2.imshow("gray2", imgR)

    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)
    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., camera_configs.Q)

    cv2.imshow("pic1", img1_rectified)
    cv2.imshow("pic2", img2_rectified)
    cv2.imshow("depth", disp)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("./snapshot/BM_left.jpg", imgL)
        cv2.imwrite("./snapshot/BM_right.jpg", imgR)
        cv2.imwrite("./snapshot/BM_depth.jpg", disp)

cv2.destroyAllWindows()