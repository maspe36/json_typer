# json-typer
Seamlessly encode and decode python objects to json while maintaining their types.

## Installation
No fancy installation at the moment. Just include the root folder in any project you're using.

## Usage
### Making a class type serializable
To make a class type serializable (a.k.a to seamlessly serialize the class to JSON and then when loading the JSON convert the object to its old type) inherit from ```python TypeSerializable``` and make sure you are passing ```python *args, **kwargs``` to the super constructor.
```python
from json-typer.serializables.type_serializable import TypeSerializable


class Foo(TypeSerializable):
    def __init__(bar, baz="", *args, **kwargs):
        self.bar = bar
        self.baz = baz
```

### Exporting a type serializable class
```python
from json-typer import io

foo = Foo(bar="example")

io.exportJSON(path=EXAMPLE_FILE, data=foo)
```

EXAMPLE_FILE contents
```javascript
{
    "type": "Foo"
    "module": "Foo"
    "bar": "example",
    "baz": ""
}
```

### Importing a JSON file
```python
from json-typer import io


foo = io.loadJSON(path=EXAMPLE_FILE)
```

Access the loaded attributes like you normally would
```python
foo.bar
>>> example

isinstance(foo, Foo)
>>> True
```

## Limitations
- Currently restricted to Python 3
    - Issue for this [here](https://github.com/maspe36/json-typer/issues/1)
- Must have ```python *args, **kwargs``` in the constructor and passed to the super call in any class that inherits from ```python TypeSerializable```

## Authors
* **Sam Privett** - *Initial work* - [maspe36](https://github.com/maspe36)

## License
This project is licensed under the LGPL License - see the [LICENSE.md](LICENSE.md) file for details
