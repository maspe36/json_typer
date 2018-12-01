# json_typer
Seamlessly encode and decode python objects to json while maintaining their types.

## Installation
No fancy installation at the moment. Just include the root folder in any project you're using.

## Usage
### Making a class type serializable
To make a class type serializable (a.k.a to seamlessly serialize the class to JSON and then when loading the JSON convert the object to its old type) inherit from ```TypeSerializable``` and make sure you are passing ```*args, **kwargs``` to the super constructor.
```python
from json_typer.serializables.type_serializable import TypeSerializable


class Foo(TypeSerializable):
    def __init__(bar, baz="", *args, **kwargs):
        self.bar = bar
        self.baz = baz
```

### Exporting a type serializable class
```python
from json_typer import io

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
from json_typer import io


foo = io.loadJSON(path=EXAMPLE_FILE)
```

Access the loaded attributes like you normally would
```python
foo.bar
>>> example

isinstance(foo, Foo)
>>> True
```

## Running Tests
Open a terminal in this projects root directory and type ```python -m unittest```

## Limitations
- Must have ```*args, **kwargs``` in the constructor and passed to the super call in any class that inherits from ```TypeSerializable```
- A class that inherits from ```TypeSerializable``` cannot implement ```_type``` or ```_module``` attributes

## Authors
* **Sam Privett** - *Initial work* - [maspe36](https://github.com/maspe36)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
