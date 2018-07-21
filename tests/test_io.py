import json
import unittest

from json_typer import io
from tests.constants import FILE_PATH, EXAMPLE_JSON
from tests.test_classes.bar import Bar
from tests.test_classes.foo import Foo
from tests.test_classes.holder import Holder


class TestIO(unittest.TestCase):
    def setUp(self):
        self.holder = Holder()
        self.holder.objects.append(Foo())
        self.holder.objects.append(Bar())

    def test_serialization(self):
        io.exportJSON(path=FILE_PATH, data=self.holder)

        with open(FILE_PATH, "r") as new_file:
            text = new_file.read()
            self.assertEqual(EXAMPLE_JSON, text)

    def test_importing(self):
        JSONDict = json.loads(EXAMPLE_JSON)
        loadedHolder = io.dictToObjects(JSONDict)

        self.assertEqual(loadedHolder, self.holder)

    def test_serialization_and_importing(self):
        io.exportJSON(path=FILE_PATH, data=self.holder)
        loadedHolder = io.loadJSON(path=FILE_PATH)

        self.assertEqual(loadedHolder, self.holder)
