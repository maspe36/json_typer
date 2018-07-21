from json_typer.serializables.type_serializable import TypeSerializable


class Holder(TypeSerializable):
    def __init__(self, objects=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not objects:
            objects = []

        self.objects = objects
