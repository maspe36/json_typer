from json_typer.serializables.type_serializable import TypeSerializable


class Foo(TypeSerializable):
    def __init__(self, *args, **kwargs):
        super(Foo, self).__init__(*args, **kwargs)
