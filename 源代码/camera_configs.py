# filename: camera_configs.py
import cv2
import numpy as np

left_camera_matrix = np.array([[3213.08, 0., 600.64723],
                               [0.,3060.75, 186.58058],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.1426, -0.4962, -0.0150, -0.0744, 0.00000]])

right_camera_matrix = np.array([[3096.37, 0., 400.00856],
                                [0., 3090.52, 269.37140],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.5450, -0.2870, -0.0110, -0.0329, 0.00000]])

om = np.array([0.01911, 0.03125, -0.00960])  # 旋转关系向量
R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-70.59612, -2.60704, 18.87635])  # 平移关系向量

# left_camera_matrix = np.array([[4213.08, 0., 251.64723],
#                                [0.,4060.75, 286.58058],
#                                [0., 0., 1.]])
# left_distortion = np.array([[-0.1426, -0.4962, -0.0150, -0.0744, 0.00000]])
#
# right_camera_matrix = np.array([[3096.37, 0., 217.00856],
#                                 [0., 3090.52, 269.37140],
#                                 [0., 0., 1.]])
# right_distortion = np.array([[-0.5450, -0.2870, -0.0110, -0.0329, 0.00000]])
# om = np.array([0.01911, 0.03125, -0.00960])  # 旋转关系向量
# R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
# T = np.array([-70.59612, -2.60704, 18.87635])  # 平移关系向量

size = (512,384)  # 图像尺寸

# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,right_camera_matrix, right_distortion, size, R,T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)