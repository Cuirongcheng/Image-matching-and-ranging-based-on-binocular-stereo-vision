# 基于双目立体视觉的图像匹配与测距

# Image-matching-and-ranging-based-on-binocular-stereo-vision

## 摘要
双目立体视觉是计算机视觉范畴的核心之一，它利用双目相机来获得目标物体的图像，经过物体图像处理之后得到目标物体所在场景环境的三维信息，最终实现非接触条件下测距，简单便捷。本次毕业设计主要内容为研究 基于双目立体视觉平台上的图像匹配以及目标物体的距离测量技术，图像特征提取部分研究了 SIFT 算法和 SURF 算 法，特征匹配部分研究了 BF 法和 FLANN 法，距离测量研究主要通过视差深度的计算，结合视觉坐标系的转换实现 三维位置的定位与测量。结合维视双目立体视觉测量平台 MV-VS220，通过 Python+OpenCV 设计实现一个具备图像 采集、图像匹配以及距离测量等功能的原型演示系统。系统可实现对关键环节的过程与结果的演示，以及不同算法的 性能比较。系统测试表明，所开发的原型演示系统从界面、功能与性能方面均达到了设计的要求。

## 关键字
双目立体视觉 图像匹配 双目测距 MV-VS220 平台 OpenCV

## Abstract
Binocular stereo vision is one of the core of computer vision. It uses binocular camera to obtain the image of the target object. After the object image is processed, the three-dimensional information of the scene environment where the target object is located is obtained, and finally the distance measurement under non-contact conditions is realized. The main content of this graduation project is to study the image matching based on the binocular stereo vision platform and the distance measurement technology of the target object. The image feature extraction part studies the SIFT algorithm and the SURF algorithm. The feature matching part studies the BF method and the FLANN method. The measurement research mainly realizes the positioning and measurement of the three-dimensional position by the calculation of the parallax depth and the transformation of the visual coordinate system. Combined with the Vision-based binocular stereo vision measurement platform MV-VS220, a prototype demonstration system with image acquisition, image matching and distance measurement is realized through Python+OpenCV design. The system can demonstrate the process and results of key parts and the performance comparison of different algorithms. System tests show that the prototype demonstration system developed meets the design requirements in terms of interface, function and performance. 

## Key Words
Binocular stereo vision   Image Matching   Binocular Distance Measurement   MV-VS220 Platform   OpenCV 

## 研究背景和意义
人类通过感觉器官获取的外部世界信息里有80%是来自视觉。研究生物视觉系统发现，双目是生物具有视觉的重要前提。以人为例，当人用两眼分别观察视野前方的物体时，会发现左眼和右眼观察到的物体在距离和方位上不大一致，这就是视差。通过视差对比分析，才能更好地研究物体在实际世界的中位置。
由于双目立体视觉系统是通过模拟人的双眼来进行感知这一原理，因此在实际中只需要两个相机，并将它们像人的双眼一样，安装在同一水平线上经过简单校正之后就可以投入使用。实现方式相对简单，使用成本低廉。因此，本文通过对双目立体视觉系统的研究，可以更好地理解图像特征提取与匹配的算法原理和效率，并且实现在非接触条件下快速准确测量。

## 主要研究内容
（1）在对相机成像和坐标系原理研究的基础上，依托维视双目立体视觉测量平台MV-VS220实现了双目相机标定，以及目标物体图像数据采集。

（2）在灰度化、二值化以及加噪等必要图像预处理的基础上，研究SIFT、SURF特征点提取与匹配算法，进行实验并显示提取和匹配效果；研究测距模型和视差深度计算目标物体的深度信息，进行实验并获取测量结果，对测量误差进行分析与讨论。

（3）基于维视双目立体视觉测量平台MV-VS220，采用Python+OpenCV开发工具，设计实现了一个双目立体视觉图像匹配与测距原型系统，可实现对关键环节的过程与结果的演示，以及不同算法的性能比较。