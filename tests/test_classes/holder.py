from json_typer.serializables.type_serializable import TypeSerializable


class Holder(TypeSerializable):
    def __init__(self, *args, **kwargs):
        super(Holder, self).__init__(*args, **kwargs)

        self.objects = []
