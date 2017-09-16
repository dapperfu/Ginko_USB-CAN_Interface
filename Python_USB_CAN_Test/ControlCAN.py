"""
Program test environment
Pyhone version:3.4.1
Firmware version:2.8.28
Dependent files(MacOSX):libGinkgo_Driver.dylib,libusb-0.1.4.dylib,libusb-1.0.0.dylib
Dependent files(Windows):Ginkgo_Driver.dll
Dependent files(Linux):libGinkgo_Driver.so,libusb-1.0.so
More Infomation:www.viewtool.com
"""
import ctypes
import platform
# Compatible with other CAN adapter datatype


class VCI_BOARD_INFO(ctypes.Structure):
    _fields_ = [
        # hardware version, in hex format, for example: 0x0100 present version is 1.00
        ("hw_Version", ctypes.c_ushort),
        ("fw_Version", ctypes.c_ushort),    # firmware version in hex format
        ("dr_Version", ctypes.c_ushort),    # driver version, in hex format
        ("in_Version", ctypes.c_ushort),    # interface library version, in hex format
        ("irq_Num", ctypes.c_ushort),        # interrupt number used by board
        ("can_Num", ctypes.c_ubyte),        # CAN channel number
        ("str_Serial_Num", ctypes.c_ubyte * 20),    # CAN board serial number
        # string for hardware type,for example:"USBCAN V1.00\0"(note:include string null end'\0').
        ("str_hw_Type", ctypes.c_ubyte * 40),
        ("Reserved", ctypes.c_ushort * 4)
    ];
# Compatible with other CAN adapter datatype


class VCI_BOARD_INFO_EX(ctypes.Structure):
    _fields_ = [
        # hardware name,for example: "Ginkgo-CAN-Adaptor\0"(note: include string null end'\0')
        ("ProductName", ctypes.c_ubyte * 32),
        ("FirmwareVersion", ctypes.c_ubyte * 4),    # firmware version
        ("HardwareVersion", ctypes.c_ubyte * 4),    # hardware version
        ("SerialNumber", ctypes.c_ubyte * 12)    # adatper serial number
    ];
# Definition of CAN frame


class VCI_CAN_OBJ(ctypes.Structure):
    _fields_ = [("ID", ctypes.c_uint),    # Frame ID
                # timestamp of the frame arriving,started from initialization of CAN controller
                ("TimeStamp", ctypes.c_uint),
                # if using timestamp. 1: use TimeStamp, 0:not use. TimeFlag and TimeStamp is available when the frame is recived frame
                ("TimeFlag", ctypes.c_byte),
                # send frame type. 0: normal send,1: single send,2: self send/receive,3: single self send/receive
                ("SendType", ctypes.c_byte),
                ("RemoteFlag", ctypes.c_byte),    # remote frame flag
                ("ExternFlag", ctypes.c_byte),    # extended frame flag
                # Data length(<=8),how many uint8_ts of data
                ("DataLen", ctypes.c_byte),
                ("Data", ctypes.c_byte * 8),      # text data
                ("Reserved", ctypes.c_byte * 3)    # reserved
                ];
# definition of CAN controller status


class VCI_CAN_STATUS(ctypes.Structure):
    _fields_ = [("ErrInterrupt", ctypes.c_byte),    # interrupt record,will be cleared while reading
                ("regMode", ctypes.c_byte),        # CAN controller mode register
                ("regStatus", ctypes.c_byte),        # CAN controller status register
                # CAN controller arbitrator lost register
                ("regALCapture", ctypes.c_byte),
                ("regECCapture", ctypes.c_byte),    # CAN controller error register
                # CAN controller error alarm limitation register
                ("regEWLimit", ctypes.c_byte),
                # CAN controller receive error register
                ("regRECounter", ctypes.c_byte),
                # CAN controller send error register
                ("regTECounter", ctypes.c_byte),
                ("regESR", ctypes.c_uint),              # CAN controller status register
                ("regTSR", ctypes.c_uint),              # CAN controller status register
                # CAN controller receive buffer size
                ("BufferSize", ctypes.c_uint),
                ("Reserved", ctypes.c_uint),        #
                ]

# definition of error data type


class VCI_ERR_INFO(ctypes.Structure):
    _fields_ = [("ErrCode", ctypes.c_uint),            # error code
                # error identification data when error has passive error
                ("Passive_ErrData", ctypes.c_ubyte * 3),
                # error identification data when error has arbitration lost error
                ("ArLost_ErrData", ctypes.c_ubyte)
                ]
# definition of CAN initialization data type


class VCI_INIT_CONFIG(ctypes.Structure):
    _fields_ = [("AccCode", ctypes.c_uint),            # ACC code (for verification)
                ("AccMask", ctypes.c_uint),        # Mask code
                ("Reserved", ctypes.c_uint),        #
                # filter type.0: double filter,1: single filter
                ("Filter", ctypes.c_byte),
                ("Timing0", ctypes.c_byte),        # Timer 0
                ("Timing1", ctypes.c_byte),        # Timer 1
                ("Mode", ctypes.c_byte)
                ];
# Definition of CAN initialization data type


class VCI_INIT_CONFIG_EX(ctypes.Structure):
    _fields_ = [("CAN_BRP", ctypes.c_uint),  # range: 1~1024, CAN baudrate = 36MHz/(CAN_BRP)/(CAN_SJW+CAN_BS1+CAN_BS2)
                ("CAN_SJW", ctypes.c_byte),    # range: 1~4
                ("CAN_BS1", ctypes.c_byte),    # range: 1~16
                ("CAN_BS2", ctypes.c_byte),     # range: 1~8
                # CAN working mode. 0: normal,1: loopback,2: silent,3: silent loopback
                ("CAN_Mode", ctypes.c_byte),
                # auto off line management. 0: prohibit,1: enable
                ("CAN_ABOM", ctypes.c_byte),
                # text repeat send management. 0: enable text repeat sending,1: disable text repeat sending
                ("CAN_NART", ctypes.c_byte),
                # FIFO lock management. 0: new text overwrite old, 1: ignore new text
                ("CAN_RFLM", ctypes.c_byte),
                # send priority management, 0: by ID, 1: by order
                ("CAN_TXFP", ctypes.c_byte),
                # relay feature enable. 0x00: close relay function,0x10: relay from CAN1 to CAN2,0x01: relay from CAN2 to CAN1, 0x11: bidirectionaly relay
                ("CAN_RELAY", ctypes.c_byte),
                ("Reserved", ctypes.c_uint)    # reserved
                ];
# definition of CAN filter setting


class VCI_FILTER_CONFIG(ctypes.Structure):
    _fields_ = [("Enable", ctypes.c_byte),            # filter enable. 1: enable,0: disable
                ("FilterIndex", ctypes.c_byte),    # filter index. range: 0~13
                # filter mode.0: mask bit,1: id list
                ("FilterMode", ctypes.c_byte),
                # filter frame flag. 1: the frame to be filtered is extended frame,0: the frame to be filtered is standard frame
                ("ExtFrame", ctypes.c_byte),
                ("ID_Std_Ext", ctypes.c_uint),        # verification code ID
                ("ID_IDE", ctypes.c_uint),        # verification code IDE
                ("ID_RTR", ctypes.c_uint),        # verification code RTR
                # Mask code ID,only available when filter mode set to mask bit mode
                ("MASK_Std_Ext", ctypes.c_uint),
                # Mask code IDE,only available when filter mode set to mask bit mode
                ("MASK_IDE", ctypes.c_uint),
                # Mask code RTR,only available when filter mode set to mask bit mode
                ("MASK_RTR", ctypes.c_uint),
                ("Reserved", ctypes.c_uint),        # reserved
                ];


# definition of CAN receive callback
if(platform.system() == "Windows"):
    PVCI_RECEIVE_CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
else:
    PVCI_RECEIVE_CALLBACK = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)

# CAN type definition
VCI_USBCAN1 = 3
VCI_USBCAN2 = 4

# CAN error code
ERR_CAN_OVERFLOW = 0x0001    # CAN controller internal FIFO overflow
ERR_CAN_ERRALARM = 0x0002    # CAN controller error alarm
ERR_CAN_PASSIVE = 0x0004    # CAN controller passive error
ERR_CAN_LOSE = 0x0008    # CAN controller arbitration lost
ERR_CAN_BUSERR = 0x0010    # CAN arbitration bus error
ERR_CAN_BUSOFF = 0x0020    # CAN arbitration bus off

# Generic error code
ERR_DEVICEOPENED = 0x0100    # Device is opened
ERR_DEVICEOPEN = 0x0200    # Device open failed
ERR_DEVICENOTOPEN = 0x0400    # Device not open
ERR_BUFFEROVERFLOW = 0x0800    # Buffer overflow
ERR_DEVICENOTEXIST = 0x1000    # Device is not exist
ERR_LOADKERNELDLL = 0x2000    # Load dll failed
ERR_CMDFAILED = 0x4000    # Command execution failed
ERR_BUFFERCREATE = 0x8000    # Memory is not enough

# Function return status
STATUS_OK = 0x01
STATUS_ERR = 0x00

import os

root = os.path.dirname(__file__)

# Import library
if(platform.system() == "Windows"):
    if "64bit" in platform.architecture():
        lib = os.path.join(root, "lib", "windows", "64bit", "Ginkgo_Driver.dll")
        GinkgoLib = ctypes.cdll.LoadLibrary(lib)
    else:
        lib = os.path.join(root, "lib", "windows", "32bit", "Ginkgo_Driver.dll")
        GinkgoLib = ctypes.cdll.LoadLibrary(lib)
elif(platform.system() == "Darwin"):
        lib = os.path.join(root, "lib", "macos", "libGinkgo_Driver.dylib")
        GinkgoLib = ctypes.cdll.LoadLibrary(lib)
elif(platform.system() == "Linux"):
    if "64bit" in platform.architecture():
        lib = os.path.join(root, "lib", "linux", "64bit", "libGinkgo_Driver.so")
        GinkgoLib = ctypes.cdll.LoadLibrary(lib)
    else:
        lib = os.path.join(root, "lib", "linux", "32bit", "libGinkgo_Driver.so")
        GinkgoLib = ctypes.cdll.LoadLibrary(lib)
else:
    print("Unknown system")
# Scan device


def VCI_ScanDevice(NeedInit=1):
    return GinkgoLib.VCI_ScanDevice(ctypes.c_ubyte(NeedInit))
# Open device


def VCI_OpenDevice(DevType, DevIndex, Reserved):
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_OpenDevice(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(Reserved))

# Close device


def VCI_CloseDevice(DevType, DevIndex):
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_CloseDevice(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex))
# Initialize device


def VCI_InitCAN(DevType, DevIndex, CANIndex, pInitConfig):
    'Initialize device'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_InitCAN(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pInitConfig)
# Initialize device extend


def VCI_InitCANEx(DevType, DevIndex, CANIndex, pInitConfig):
    'Initialize device extend'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_InitCANEx(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pInitConfig)
# Get board infomation


def VCI_ReadBoardInfoEx(DevIndex, pInfo):
    'Get board infomation'
    return GinkgoLib.VCI_ReadBoardInfoEx(ctypes.c_uint(DevIndex), pInfo)
# Get CAN status


def VCI_ReadCANStatus(DevType, DevIndex, CANIndex, pCANStatus):
    'Get CAN status'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_ReadCANStatus(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pCANStatus)

# Set CAN filter


def VCI_SetFilter(DevType, DevIndex, CANIndex, pFilter):
    'Set CAN filter'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_SetFilter(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pFilter)

# Get CAN number from buffer


def VCI_GetReceiveNum(DevType, DevIndex, CANIndex):
    'Get CAN number from buffer'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_GetReceiveNum(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex))
# Clear CAN buffer


def VCI_ClearBuffer(DevType, DevIndex, CANIndex):
    'Clear CAN buffer'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_ClearBuffer(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex))

# Register receive callback function


def VCI_RegisterReceiveCallback(DevIndex, pReceiveCallBack):
    'Register receive callback function'
    return GinkgoLib.VCI_RegisterReceiveCallback(ctypes.c_uint(DevIndex), pReceiveCallBack)

# Logout receive callback function


def VCI_LogoutReceiveCallback(DevIndex):
    'Logout receive callback function'
    return GinkgoLib.VCI_LogoutReceiveCallback(ctypes.c_uint(DevIndex))

# Start receive CAN


def VCI_StartCAN(DevType, DevIndex, CANIndex):
    'Start receive CAN'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_StartCAN(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex))

# Stop and reset CAN


def VCI_ResetCAN(DevType, DevIndex, CANIndex):
    'Stop and reset CAN'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_ResetCAN(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex))

# Transmit CAN data


def VCI_Transmit(DevType, DevIndex, CANIndex, pSend, Len):
    'Transmit CAN data'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_Transmit(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pSend, ctypes.c_uint(Len))

# Read CAN data from buffer


def VCI_Receive(DevType, DevIndex, CANIndex, pReceive, Len, WaitTime):
    'Read CAN data from buffer'
    try:
        assert DevType == VCI_USBCAN2, 'Device type error!'
        assert 0 <= CANIndex <= 1, 'CAN index error!'
    except AssertionError as args:
        print('%s: %s' % (args.__class__.__name__, args))
        exit()
    return GinkgoLib.VCI_Receive(ctypes.c_uint(DevType), ctypes.c_uint(DevIndex), ctypes.c_uint(CANIndex), pReceive, ctypes.c_uint(Len), ctypes.c_uint(WaitTime))
