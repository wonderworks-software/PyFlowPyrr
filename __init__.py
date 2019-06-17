PACKAGE_NAME = 'PyFlowPyrr'
from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.PyFlowPyrr.Pins.QuatPin import QuatPin
from PyFlow.Packages.PyFlowPyrr.Pins.FloatVector3Pin import FloatVector3Pin
from PyFlow.Packages.PyFlowPyrr.Pins.FloatVector4Pin import FloatVector4Pin
from PyFlow.Packages.PyFlowPyrr.Pins.Matrix33Pin import Matrix33Pin
from PyFlow.Packages.PyFlowPyrr.Pins.Matrix44Pin import Matrix44Pin

# Function based nodes
from PyFlow.Packages.PyFlowPyrr.FunctionLibraries.Matrix33 import Matrix33
from PyFlow.Packages.PyFlowPyrr.FunctionLibraries.Matrix44 import Matrix44
from PyFlow.Packages.PyFlowPyrr.FunctionLibraries.QuatLib import QuatLib
from PyFlow.Packages.PyFlowPyrr.FunctionLibraries.Vector3 import Vector3
from PyFlow.Packages.PyFlowPyrr.FunctionLibraries.Vector4 import Vector4

# Factories
from PyFlow.Packages.PyFlowPyrr.Factories.PinInputWidgetFactory import getInputWidget


_FOO_LIBS = {
    Matrix33.__name__: Matrix33(PACKAGE_NAME),
    Matrix44.__name__: Matrix44(PACKAGE_NAME),
    QuatLib.__name__: QuatLib(PACKAGE_NAME),
    Vector3.__name__: Vector3(PACKAGE_NAME),
    Vector4.__name__: Vector4(PACKAGE_NAME)
}

_NODES = {

}

_PINS = {
    FloatVector3Pin.__name__: FloatVector3Pin,
    FloatVector4Pin.__name__: FloatVector4Pin,
    Matrix33Pin.__name__: Matrix33Pin,
    Matrix44Pin.__name__: Matrix44Pin,
    QuatPin.__name__: QuatPin
}


_TOOLS = OrderedDict()


class PyFlowPyrr(IPackage):
    def __init__(self):
        super(PyFlowPyrr, self).__init__()

    @staticmethod
    def GetFunctionLibraries():
        return _FOO_LIBS

    @staticmethod
    def GetNodeClasses():
        return _NODES

    @staticmethod
    def GetPinClasses():
        return _PINS

    @staticmethod
    def GetToolClasses():
        return _TOOLS

    @staticmethod
    def PinsInputWidgetFactory():
        return getInputWidget
