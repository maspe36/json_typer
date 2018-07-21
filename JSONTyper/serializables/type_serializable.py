from JSONTyper.serializables.serializable import Serializable


class TypeSerializable(Serializable):
    def __init__(self, type="", module=""):
        super().__init__()
        self.type = type
        self.module = module

    def getType(self):
        return self.__class__.__name__

    def getModule(self):
        return self.__class__.__module__

    def _myattrs(self):
        self.type = self.getType()
        self.module = self.getModule()
        return super()._myattrs()
