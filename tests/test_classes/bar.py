from json_typer import TypeSerializable


class Bar(TypeSerializable):
    def __init__(self, *args, **kwargs):
        super(Bar, self).__init__(*args, **kwargs)
