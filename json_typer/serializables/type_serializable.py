from json_typer.serializables.serializable import Serializable


class TypeSerializable(Serializable):
    # Eat the kwargs that aren't named arguments in constructors
    def __init__(self, type="", module="", *args, **kwargs):
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
