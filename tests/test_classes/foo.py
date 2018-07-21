from json_typer.serializables.type_serializable import TypeSerializable


class Foo(TypeSerializable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
