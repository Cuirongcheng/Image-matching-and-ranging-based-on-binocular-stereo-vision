from ctypes import *
from GigECamera_Types import *
MVGigE = windll.LoadLibrary('MVGigE')


def MVInitLib():
    """
    初始化函数库。在调用函数所有函数之前调用。
    """
    return MVSTATUS_CODES(MVGigE.MVInitLib())


def MVTerminateLib():
    """
    退出函数库。在程序退出前调用，以释放资源。
    """
    return MVSTATUS_CODES(MVGigE.MVTerminateLib())


def MVUpdateCameraList():
    """
    查找连接到计算机上的相机
    """
    return MVSTATUS_CODES(MVGigE.MVUpdateCameraList())


class MVGetNumOfCameras():
    """
    获取连接到计算机上的相机的数量
    返回两个属性
    status：状态码
    num：相机数量
    """
    def __init__(self):
        self.init()

    def init(self):
        pNumCams = c_int()
        result = MVGigE.MVGetNumOfCameras(byref(pNumCams))
        self.status = MVSTATUS_CODES(result)
        self.num = pNumCams.value


class MVOpenCamByIndex():
    """
    打开指定idx的相机
    输入：相机的索引
    返回两个属性
    status：状态码
    hCam：相机句柄
    """
    def __init__(self, idx):
        self.idx = c_byte(idx)
        self.init()

    def init(self):
        hCam = c_int()
        result = MVGigE.MVOpenCamByIndex(self.idx, byref(hCam))
        self.status = MVSTATUS_CODES(result)
        self.hCam = hCam.value

class MVOpenCamByUserDefinedName():
    """
    打开指定的用户自定义名称的相机
    输入：相机的名称name 
    返回两个属相
    status：状态码
    hCam：相机句柄
    """
    def __init__(self):
        self.init()

    def init(self):
        name = c_char_p()
        hCam = c_char_p()
        result = MVGigE.MVOpenCamByUserDefinedName(byref(name),byref(hCam))
        self.status = MVSTATUS_CODES(result)
        self.hCam = hCam.value



class MVImageCreate():
    """"
    创建图像
    输入：图像宽度， 图像高度，  每像素Bit数
    返回一个属性
    himage：图像句柄
    """
    def __init__(self, width, height, nBPP):
        self.width = c_int(width)
        self.height = c_int(height)
        self.nBPP = c_int(nBPP)
        self.init()

    def init(self):
        result = MVGigE.MVImageCreate(self.width, self.height, self.nBPP)
        self.himage = result


class MVCloseCam():
    """
    关闭相机
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        result = MVGigE.MVCloseCam(self.hCam)
        self.status = MVSTATUS_CODES(result)


class MVGetWidth():
    """
    图像宽度[像素]
    输入：相机句柄
    返回两个属性
    status：状态码
    width：图像的宽度
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        width = c_int()
        result = MVGigE.MVGetWidth(self.hCam, byref(width))
        self.status = MVSTATUS_CODES(result)
        self.width = width.value


class MVGetHeight():
    """
    图像高度[像素]
    输入：相机句柄
    返回两个属性
    status：状态码
    height：图像的高度
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        height = c_int()
        result = MVGigE.MVGetHeight(self.hCam, byref(height))
        self.status = MVSTATUS_CODES(result)
        self.height = height.value


class MVGetPixelFormat():
    """
    读取图像的像素格式
    输入：相机句柄
    返回两个属性
    status：状态码
    pixelFormat：像素格式
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        pixelFormat = c_int()
        result = MVGigE.MVGetPixelFormat(self.hCam, byref(pixelFormat))
        self.status = MVSTATUS_CODES(result)
        self.pixelFormat = MV_PixelFormatEnums(pixelFormat.value)


class MVSetTriggerMode():
    """"
    设置触发模式
    输入：相机句柄， 触发模式[TriggerModeEnums]
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, pMode):
        self.hCam = c_int(hCam)
        self.pMode = c_int(pMode.value)
        self.init()

    def init(self):
        result = MVGigE.MVSetTriggerMode(self.hCam, self.pMode)
        self.status = MVSTATUS_CODES(result)


class MVGetTriggerMode():
    """
    读取触发模式
    输入：相机句柄
    返回两个属性
    status：状态码
    pMode：触发模式
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        pMode = c_int()
        result = MVGigE.MVGetTriggerMode(self.hCam, byref(pMode))
        self.status = MVSTATUS_CODES(result)
        self.pMode = TriggerModeEnums(pMode.value)


class MVInfo2Image():
    """
    将回调函数收到的图像信息转换为图像
    输入：相机句柄， 采集 Callback 函数中传来的图像信息指针，转换结果图像的指针
    放回两个属性
    status：状态码
    pInfo：图像句柄
    """
    def __init__(self, hCam, pImage):
        self.hCam = c_int(hCam)
        self.pImage = c_int(pImage)
        self.init()

    def init(self):
        pInfo = IMAGE_INFO()
        result = MVGigE.MVInfo2Image(
            self.hCam, byref(pInfo), byref(self.pImage))
        self.status = MVSTATUS_CODES(result)
        self.pInfo = pInfo


class MVStopGrab():
    """"
    停止采集
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        result = MVGigE.MVStopGrab(self.hCam)
        self.status = MVSTATUS_CODES(result)


class MVImageDrawHwnd():
    """
    在目标窗体上的指定位置1:1绘制本图像
    输入：相机句柄， 目标窗体，图像绘制的起始水平坐标，图像绘制的起始垂直坐标
    返回一个属性
    status：状态码
    """
    def __init__(self, himage, handle, x, y):
        self.himage = c_int(himage)
        self.handle = c_int(handle)
        self.x = c_int(x)
        self.y = c_int(y)
        self.init()

    def init(self):
        result = MVGigE.MVImageDrawHwnd(
            self.himage, self.handle, self.x, self.y)
        self.status = result


class MVImageDraw():
    """
    在目标 DC 上的指定位置1:1绘制本图像
    输入：相机句柄， 目标 DC，图像绘制的起始水平坐标，图像绘制的起始垂直坐标
    """

    def __init__(self, himage, DC, x, y):
        self.himage = c_int(himage)
        self.DC = c_int(DC)
        self.x = c_int(x)
        self.y = c_int(y)
        self.init()

    def init(self):
        MVGigE.MVImageDraw(self.himage, self.DC, self.x, self.y)


class MVSingleGrab():
    """
    采集一帧图像
    输入：相机句柄， 图像句柄，等待多长时间，单位 ms
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, himage, nWaitMs):
        self.hCam = c_int(hCam)
        self.himage = c_int(himage)
        self.nWaitMs = c_ulong(nWaitMs)
        self.init()

    def init(self):
        result = MVGigE.MVSingleGrab(self.hCam, self.himage, self.nWaitMs)
        self.status = MVSTATUS_CODES(result)


class MVImageSave():
    """
    保存图片
    输入：相机句柄， 文件名
    """

    def __init__(self, himage, fileName):
        self.himage = c_int(himage)
        self.fileName = c_char_p(fileName)
        self.init()

    def init(self):
        result = MVGigE.MVImageSave(self.himage, self.fileName)


class MVStartGrabWindow():
    """
    开始采集，并将采集到的图像显示到指定窗口
    输入：相机句柄， 窗口句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, winid):
        self.hCam = c_int(hCam)
        self.winid = c_int(winid)
        self.init()

    def init(self):
        result = MVGigE.MVStartGrabWindow(self.hCam, self.winid, c_int(0))
        self.status = MVSTATUS_CODES(result)


class MVStopGrabWindow():
    """
    停止采集到窗口
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        result = MVGigE.MVStopGrabWindow(self.hCam)
        self.status = MVSTATUS_CODES(result)


class MVFreezeGrabWindow():
    """
    当采集到窗口时，暂停或继续采集。
    输入：相机句柄， True或者False
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, bFreeze):
        self.hCam = c_int(hCam)
        self.bFreeze = c_bool(bFreeze)
        self.init()

    def init(self):
        result = MVGigE.MVFreezeGrabWindow(self.hCam, self.bFreeze)
        self.status = MVSTATUS_CODES(result)


class MVGetSampleGrab():
    """
    当调用 MVFreezeGrabWindow(TRUE)后，调用此函数可以获取当前图像。
    输入：相机句柄， 图像
    返回两个属性
    statu：状态码
    idn：图像的ID号
    """
    def __init__(self, hCam, himage):
        self.hCam = c_int(hCam)
        self.himage = c_int(himage)
        self.init()

    def init(self):
        idn = c_int()
        result = MVGigE.MVGetSampleGrab(self.hCam, self.himage, byref(idn))
        self.status = MVSTATUS_CODES(result)
        self.idn = idn.value


class MVSetGrabWindow():
    """"
    当采集到窗口时，设置图像显示的比例
    输入：相机句柄， 采集宽度， 采集高度
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, width, height):
        self.hCam = c_int(hCam)
        self.width = c_int(width)
        self.height = c_int(height)
        self.init()

    def init(self):
        result = MVGigE.MVSetGrabWindow(
            self.hCam, 0, 0, self.width, self.height, 0, 0, self.width, self.height)
        self.status = MVSTATUS_CODES(result)


class MVSetPacketSize():
    """
    设置网络数据包的大小
    输入：相机句柄， 网络数据包大小（字节）
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, psize):
        self.hCam = c_int(hCam)
        self.psize = c_int(psize)
        self.init()

    def init(self):
        result = MVGigE.MVSetPacketSize(self.hCam, self.psize)
        self.status = MVSTATUS_CODES(result)


class MVGetPacketSize():
    """
    读取网络数据包大小
    输入：相机句柄
    返回两个属性
    status：状态码
    psize：数据包大小
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        psize = c_int()
        result = MVGigE.MVGetPacketSize(self.hCam, byref(psize))
        self.status = MVSTATUS_CODES(result)
        self.psize = psize.value


class MVSetPacketDelay():
    """
    设置网络数据包之间的时间间隔。
    输入：相机句柄，时间间隔[us]
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, time_us):
        self.hCam = c_int(hCam)
        self.time_us = c_int(time_us)
        self.init()

    def init(self):
        result = MVGigE.MVSetPacketDelay(self.hCam, self.time_us)
        self.status = MVSTATUS_CODES(result)


class MVGetPacketDelay():
    """
    读取网络数据包间隔
    输入：相机句柄
    返回两个属性
    status：状态码
    time_us：数据包延迟
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        time_us = c_int()
        result = MVGigE.MVGetPacketDelay(self.hCam, byref(time_us))
        self.status = MVSTATUS_CODES(result)
        self.time_us = time_us.value


class MVTriggerSoftware():
    """
    发出软件触发指令
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        result = MVGigE.MVTriggerSoftware(self.hCam)
        self.status = MVSTATUS_CODES(result)


class MVSetTriggerSource():
    """
    设置触发源
    输入：相机句柄， 触发源
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, source):
        self.hCam = c_int(hCam)
        self.source = c_int(source)
        self.init()

    def init(self):
        result = MVGigE.MVSetTriggerSource(self.hCam, self.source)
        self.status = MVSTATUS_CODES(result)


class MVGetTriggerSource():
    """
    读取触发源
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        source = c_int()
        result = MVGigE.MVGetTriggerSource(self.hCam, byref(source))
        self.status = MVSTATUS_CODES(result)
        self.source = TriggerSourceEnums(source.value)


class MVSetTriggerActivation():
    """
    当使用触发线触发时,设置是上升沿触发还是下降沿触发
    输入：相机句柄，上升沿或下降沿
    返回一个属性
    status：状态码
    """
    def __init__(self, hCam, act):
        self.hCam = c_int(hCam)
        self.act = c_int(act)
        self.init()

    def init(self):
        result = MVGigE.MVSetTriggerActivation(self.hCam, self.act)
        self.status = MVSTATUS_CODES(result)


class MVGetTriggerActivation():
    """
    读取触发极性
    输入：相机句柄
    返回一个属性
    status：状态码
    """
    def __init__(self,hCam):
        self.hCam = c_int(hCam)
        self.init()

    def init(self):
        act = c_int()
        result = MVGigE.MVGetTriggerActivation(self.hCam, byref(act))
        self.status = MVSTATUS_CODES(result)
        self.act = TriggerActivationEnums(act.value)
