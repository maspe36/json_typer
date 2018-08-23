from json_typer.serializables.serializable import Serializable


class TypeSerializable(Serializable):
    # Eat the kwargs that aren't named arguments in constructors
    def __init__(self, _type="", _module="", *args, **kwargs):
        super(TypeSerializable, self).__init__()
        self._type = _type
        self._module = _module

    def _getType(self):
        return self.__class__.__name__

    def _getModule(self):
        return self.__class__.__module__

    def _myattrs(self):
        self._type = self._getType()
        self._module = self._getModule()
        return super(TypeSerializable, self)._myattrs()
