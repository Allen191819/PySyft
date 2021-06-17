# stdlib
import functools
from typing import Any as TypeAny
from typing import List as TypeList
from typing import Tuple as TypeTuple

# third party
import pycolab
from pycolab import ascii_art
from pycolab import engine
from pycolab import prefab_parts
from pycolab import things
from pycolab.prefab_parts import drapes
from pycolab.prefab_parts import sprites

# syft relative
# from . import engine  # noqa: 401
from ...ast import add_classes
from ...ast import add_methods
from ...ast import add_modules
from ...ast.globals import Globals
from ..util import generic_update_ast

LIB_NAME = "pycolab"
PACKAGE_SUPPORT = {"lib": LIB_NAME}


def create_ast(client: TypeAny = None) -> Globals:
    ast = Globals(client)

    modules: TypeList[TypeTuple[str, TypeAny]] = [
        ("pycolab", pycolab),
        ("pycolab.engine", engine),
        ("pycolab.ascii_art", ascii_art),
        ("pycolab.things", things),
        ("pycolab.prefab_parts", prefab_parts),
        ("pycolab.prefab_parts.drapes", drapes),
        ("pycolab.prefab_parts.sprites", sprites),
    ]

    classes: TypeList[TypeTuple[str, str, TypeAny]] = [
        ("pycolab.engine.Engine", "pycolab.engine.Engine", engine.Engine),
        ("pycolab.ascii_art.Partial", "pycolab.ascii_art.Partial", ascii_art.Partial),
        ("pycolab.things.Drape", "pycolab.things.Drape", things.Drape),
        ("pycolab.things.Sprite", "pycolab.things.Sprite", things.Sprite),
        (
            "pycolab.prefab_parts.drapes.Scrolly",
            "pycolab.prefab_parts.drapes.Scrolly",
            drapes.Scrolly,
        ),
        (
            "pycolab.prefab_parts.sprites.MazeWalker",
            "pycolab.prefab_parts.sprites.MazeWalker",
            sprites.MazeWalker,
        ),
    ]

    methods: TypeList[TypeTuple[str, str]] = [
        ("pycolab.ascii_art.ascii_art_to_game", "pycolab.engine.Engine"),
        ("pycolab.things.Drape.update", "syft.lib.python._SyNone"),
        ("pycolab.things.Sprite.update", "syft.lib.python._SyNone"),
    ]

    add_modules(ast, modules)
    add_classes(ast, classes)
    add_methods(ast, methods)

    for klass in ast.classes:
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_storable_object_attr_convenience_methods()

    return ast


update_ast = functools.partial(generic_update_ast, LIB_NAME, create_ast)
