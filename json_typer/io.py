import importlib
import json

TYPE = "type"
MODULE = "module"


def exportJSON(path, data):
    with open(path, "w") as file:
        json.dump(data, file)


def loadJSON(path):
    with open(path, "r") as data:
        JSON = json.load(data)
        return dictToObjects(JSON)


def dictToObjects(JSON):
    for key, value in JSON.items():
        if isinstance(value, list):
            for child in value:
                value[value.index(child)] = dictToObjects(child)

        if isDecodable(value):
            JSON[key] = dictToObjects(value)

    if isDecodable(JSON):
        return createObject(JSON)


def isDecodable(value):
    return isinstance(value, dict) and TYPE in value and MODULE in value


def createObject(JSON):
    objectType = JSON[TYPE]
    module = JSON[MODULE]
    importedModule = importlib.import_module(module)
    return getattr(importedModule, objectType)(**JSON)