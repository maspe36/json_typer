from json_typer import TypeSerializable


class Foo(TypeSerializable):
    def __init__(self, *args, **kwargs):
        super(Foo, self).__init__(*args, **kwargs)
