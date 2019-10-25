from enum import Enum
from ctypes import *


# 回调函数得到的数据结构
class IMAGE_INFO(Structure):
    _fields_ = [('nTimeStamp', c_ulonglong),         # 时间戳，采集到图像的时刻，精度为0.01us
                ('nBlockId', c_ushort),              # 帧号，从开始采集开始计数
                ('pImageBuffer', POINTER(c_ubyte)),  # 图像指针，即指向(0,0)像素所在内存位置的指针，通过该指针可以访问整个图
                ('nImageSizeAcq', c_ulong),          # 采集到的图像大小[字节]
                ('nMissingPackets', c_ubyte),        # 传输过程中丢掉的包数量
                ('nPixelType', c_ulonglong),         # 图像格式
                ('nSizeX', c_uint),                  # 图像宽度
                ('nSizeY', c_uint),                  # 图像高度
                ('nOffsetX', c_uint),                # 图像水平坐标
                ('nOffsetY', c_uint)]                # 图像垂直坐标


# Bayer颜色模式
class MV_BAYER_MODE(Enum):
    BayerRG = 0   # 颜色模式RGGB
    BayerBG = 1   # 颜色模式BGGR
    BayerGR = 2   # 颜色模式GRBG
    BayerGB = 3   # 颜色模式GBRG
    BayerGRW = 4  # 颜色模式GRW
    BayerInvalid = 5


# 图像的像素格式
class MV_PixelFormatEnums(Enum):
    PixelFormat_Mono8 = 0x01080001      # 8Bit灰度
    PixelFormat_BayerBG8 = 0x0108000B   # 8Bit Bayer图,颜色模式为BGGR
    PixelFormat_BayerRG8 = 0x01080009   # 8Bit Bayer图,颜色模式为RGGB
    PixelFormat_BayerGB8 = 0x0108000A   # 8Bit Bayer图,颜色模式为GBRG
    PixelFormat_BayerGR8 = 0x01080008   # 8Bit Bayer图,颜色模式为GRBG
    PixelFormat_BayerGRW8 = 0x0108000C  # 8Bit Bayer图,颜色模式为GRW8
    PixelFormat_Mono16 = 0x01100007     # 16Bit灰度
    PixelFormat_BayerGR16 = 0x0110002E  # 16Bit Bayer图,颜色模式为GR
    PixelFormat_BayerRG16 = 0x0110002F  # 16Bit Bayer图,颜色模式为RG
    PixelFormat_BayerGB16 = 0x01100030  # 16Bit Bayer图,颜色模式为GB
    PixelFormat_BayerBG16 = 0x01100031  # 16Bit Bayer图,颜色模式为BG


# 错误返回值类型
class MVSTATUS_CODES(Enum):
    MVST_SUCCESS = 0                  # 没有错误
    MVST_ERROR = -1001                # 一般错误
    MVST_ERR_NOT_INITIALIZED = -1002  # 没有初始化
    MVST_ERR_NOT_IMPLEMENTED = -1003  # 没有实现
    MVST_ERR_RESOURCE_IN_USE = -1004  # 资源被占用
    MVST_ACCESS_DENIED = -1005        # 无法访问
    MVST_INVALID_HANDLE = -1006       # 错误句柄
    MVST_INVALID_ID = -1007           # 错误ID
    MVST_NO_DATA = -1008              # 没有数据
    MVST_INVALID_PARAMETER = -1009    # 错误参数
    MVST_FILE_IO = -1010              # IO错误
    MVST_TIMEOUT = -1011              # 超时
    MVST_ERR_ABORT = -1012            # 退出
    MVST_INVALID_BUFFER_SIZE = -1013  # 缓冲区尺寸错误
    MVST_ERR_NOT_AVAILABLE = -1014    # 无法访问
    MVST_INVALID_ADDRESS = -1015      # 地址错误


# 相机的信息
class MVCamInfo(Structure):
    _fields_ = [('mIpAddr', c_ubyte*4),           # 相机的IP地址
                ('mEthernetAddr', c_ubyte*6),     # 相机的MAC地址
                ('mMfgName', c_char*32),          # 相机的厂商名称
                ('mModelName', c_char*32),        # 相机型号
                ('mSerialNumber', c_char*32),     # 相机序列号
                ('mUserDefinedName', c_char*16),  # 用户设置相机名称
                ('m_IfIP', c_ubyte*4),            # 计算机和相机连接网卡IP地址
                ('m_IfMAC', c_ubyte*6)]           # 计算机和相机连接的网卡MAC地址


# 相机的采集模式
class TriggerModeEnums(Enum):
    TriggerMode_Off = 0  # 触发模式关，即FreeRun模式，相机连续采集
    TriggerMode_On = 1   # 触发模式开，相机等待软触发或外触发信号再采集图像


# 相机的触发模式控制
class TriggerSourceEnums(Enum):
    TriggerSource_Software = 0  # 触发模式下，由软触发(软件指令)来触发采集
    TriggerSource_Line1 = 2     # 触发模式下，有外触发信号来触发采集


# 外触发触发模式的控制
class TriggerActivationEnums(Enum):
    TriggerActivation_RisingEdge = 0   # 上升沿触发
    TriggerActivation_FallingEdge = 1  # 下降沿触发


class LineSourceEnums(Enum):
    LineSource_Off = 0             # 关闭
    LineSource_ExposureActive = 5  # 和曝光同时
    LineSource_Timer1Active = 6    # 由定时器控制
    LineSource_UserOutput0 = 12    # 直接由软件控制


class MVStreamStatistic(Structure):
    _fields_ = [('m_nTotalBuf', c_ulong),         # 从开始采集，总计成功收到的完成图像帧数
                ('m_nFailedBuf', c_ulong),        # 从开始采集，总计收到的不完成图像帧数
                ('m_nTotalPacket', c_ulong),      # 从开始采集，总计收到的图像数据包数
                ('m_nFailedPacket', c_ulong),     # 从开始采集，总计丢失的图像包数
                ('m_nResendPacketReq', c_ulong),  # 从开始采集，总计重发请求的图像数据包数
                ('m_nResendPacket', c_ulong)]     # 从开始采集，总计重发成功的图像数据包数


# 用户设置选项
class UserSetSelectorEnums(Enum):
    UserSetSelector_Default = 0   # 出厂设置
    UserSetSelector_UserSet1 = 1  # 用户设置1
    UserSetSelector_UserSet2 = 2  # 用户设置2


class SensorTapsEnums(Enum):
    SensorTaps_One = 1    # 单通道
    SensorTaps_Two = 2    # 双通道
    SensorTaps_Three = 3  # 三通道
    SensorTaps_Four = 4   # 四通道


class AutoFunctionProfileEnums(Enum):
    AutoFunctionProfile_GainMinimum = 0      # 保持增益为最小值
    AutoFunctionProfile_ExposureMinimum = 1  # 曝光时间为最小值


class GainAutoEnums(Enum):
    GainAuto_Off = 0         # 关闭自动增益调整
    GainAuto_Once = 1        # 自动增益调整一次
    GainAuto_Continuous = 2  # 自动增益持续调整


class ExposureAutoEnums(Enum):
    ExposureAuto_Off = 0         # 自动曝光时间关闭调整
    ExposureAuto_Once = 1        # 曝光时间自动调整一次
    ExposureAuto_Continuous = 2  # 曝光时间自动持续调整


class BalanceWhiteAutoEnums(Enum):
    BalanceWhiteAuto_Off = 0         # 关闭自动白平衡调整
    BalanceWhiteAuto_Once = 1        # 自动白平衡调整一次
    BalanceWhiteAuto_Continuous = 2  # 自动白平衡持续调整


class ImageRotateType(Enum):
    Rotate90DegCw = 0   # 顺时针旋转90度
    Rotate90DegCcw = 1  # 逆时针旋转90度


class ImageFlipType(Enum):
    FlipHorizontal = 0  # 左右翻转
    FlipVertical = 1    # 上下翻转
    FlipBoth = 2        # 旋转180度


class TransferControlModeEnums(Enum):
    TransferControlMode_Basic = 0
    TransferControlMode_UserControlled = 2


class EventIdEnum(Enum):
    EVID_LOST = 0       # 事件ID，相机断开
    EVID_RECONNECT = 1  # 事件ID，相机重新连上了
