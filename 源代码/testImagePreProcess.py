#-*- coding: utf-8 -*-
import cv2
import numpy as np
import time
# fn = "./img/01.bmp"
fn = "./img/image4.jpg"


if __name__ == '__main__':
    print('loading %s' % fn)
    img = cv2.imread(fn)
    sp = img.shape
    print(sp)

    # 获取图像大小
    sz1 = sp[0]
    sz2 = sp[1]
    print('width:%d\nheight:%d' % (sz2,sz1))

    # imga
    # 创建一个窗口显示图像
    cv2.imshow('imga', img)

    # a-sift
    # 设置算法运行开始时间
    start = time.clock()
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img, None)  # 找到关键点
    print('a-sift feature number:',len(kp))
    img0 = cv2.drawKeypoints(img, kp, img)  # 绘制关键点
    cv2.imshow('imgasift',img)
    a_sift_time = (time.clock() - start)
    print("a-sift time used:", '% 4f' % (a_sift_time*1000))
    print('% 4f' % (a_sift_time*1000/len(kp)))

    # a-surf
    # 设置算法运行开始时间
    start = time.clock()
    surf = cv2.xfeatures2d.SURF_create(400)
    key_query = surf.detect(img, None)
    print('a-surf feature number:',len(key_query))
    img02 = cv2.drawKeypoints(img,key_query,img)
    cv2.imshow('imgasurf', img02)
    a_surf_time = (time.clock() - start)
    print("a-surf time used:", '% 4f' % (a_surf_time*1000))
    print('% 4f' % (a_surf_time*1000/len(key_query)))

    # imgb
    # 复制并转换为灰度化图像并显示
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('imgb', img1)

    # b-sift
    # 设置算法运行开始时间
    start = time.clock()
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img1, None)  # 找到关键点
    print('b-sift feature number:',len(kp))
    img1 = cv2.drawKeypoints(img1, kp, img1)  # 绘制关键点
    cv2.imshow('imgbsift',img1)
    b_sift_time = (time.clock() - start)
    print("b-sift time used:", '% 4f' % (b_sift_time*1000))
    print('% 4f' % (b_sift_time*1000/len(kp)))


    # b-surf
    # 设置算法运行开始时间
    start = time.clock()
    surf = cv2.xfeatures2d.SURF_create(400)
    key_query = surf.detect(img1, None)
    print('b-surf feature number:',len(key_query))
    img12 = cv2.drawKeypoints(img1, key_query, img1)
    cv2.imshow('imgbsurf', img12)
    b_surf_time = (time.clock() - start)
    print("b-surf time used:", '% 4f' % (b_surf_time*1000))
    print('% 4f' % (b_surf_time*1000 / len(key_query)))

    # imgc
    # 复制并转换为二值化图像并显示
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.threshold(img2, 140, 255, 0,img2)
    cv2.imshow("imgc", img2)

    # c-sift
    # 设置算法运行开始时间
    start = time.clock()
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img2, None)  # 找到关键点
    print('imgc-sift feature number:',len(kp))
    img2 = cv2.drawKeypoints(img2, kp, img2)  # 绘制关键点
    cv2.imshow("imgcsift", img2)
    c_sift_time = (time.clock() - start)
    print("c-sift time used:", '% 4f' % (c_sift_time*1000))
    print('% 4f' % (c_sift_time*1000 / len(kp)))

    # c-surf
    # 设置算法运行开始时间
    start = time.clock()
    surf = cv2.xfeatures2d.SURF_create(400)
    key_query = surf.detect(img2, None)
    print('c-surf feature number:',len(key_query))
    img22 = cv2.drawKeypoints(img2, key_query, img2)
    cv2.imshow('imgcsurf', img22)
    c_surf_time = (time.clock() - start)
    print("c-surf time used:",'% 4f' % (c_surf_time*1000))
    print('% 4f' % (c_surf_time*1000 / len(key_query)))

    # imgd
    # 噪声点数量
    img3 = img.copy()
    coutn = 10000
    for k in range(0, coutn):
        # 获取图像噪声点的随机位置
        xi = int(np.random.uniform(0, img3.shape[1]))
        xj = int(np.random.uniform(0, img3.shape[0]))
        # 加噪
        if img3.ndim == 2:
            # 灰度图像
            img3[xj, xi] = 255
        elif img3.ndim == 3:
            # 非灰度图像，图像加噪
            img3[xj, xi, 0] = 25
            img3[xj, xi, 1] = 20
            img3[xj, xi, 2] = 20
    cv2.imshow('imgd', img3)

    # d-sift
    # 设置算法运行开始时间
    start = time.clock()
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img3, None)  # 找到关键点
    print('d-sift feature number:',len(kp))
    img3 = cv2.drawKeypoints(img3, kp, img3)  # 绘制关键点
    cv2.imshow('imgdsift', img3)
    d_sift_time = (time.clock() - start)
    print("d-sift time used:", '% 4f' % (d_sift_time*1000))
    print('% 4f' % (c_sift_time*1000 / len(kp)))

    # d-surf
    # 设置算法运行开始时间
    start = time.clock()
    surf = cv2.xfeatures2d.SURF_create(400)
    key_query = surf.detect(img3, None)
    print('d-surf feature number:',len(key_query))
    img32 = cv2.drawKeypoints(img3, key_query, img3)
    cv2.imshow('imgdsurf', img32)
    d_surf_time = (time.clock() - start)
    print("d-surf time used:", '% 4f' % (d_surf_time*1000))
    print('% 4f' % (d_surf_time*1000 / len(key_query)))

    cv2.waitKey(0)
    cv2.destroyAllWindows()