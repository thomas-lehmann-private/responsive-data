"""Module data.

The MIT License

Copyright 2022 Thomas Lehmann.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
# pylint: disable=too-few-public-methods
from responsive.wrapper import DictWrapper, ListWrapper


def __apply_wrapper(root: object, parent: object) -> None:
    """Modify recursive object to be responsive.

    Args:
        root (object): the main object that should be responsive
        parant (object): the current parent in the hierachy (None if root)
    """
    current = parent if parent is not None else root
    the_dict = None

    if isinstance(current, DictWrapper):
        __apply_wrapper(current, current.obj)
        return

    the_dict = current if isinstance(current, dict) else current.__dict__

    for key, value in the_dict.items():
        current_type = type(value)
        if str(current_type).startswith("<class"):
            if not current_type.__module__ == "builtins" or isinstance(value, dict):
                wrapped_value = DictWrapper(value)
                __apply_wrapper(root, wrapped_value)
                wrapped_value.add_observer(root)
                the_dict[key] = wrapped_value
            elif isinstance(value, list):
                wrapped_value = ListWrapper(value)
                wrapped_value.add_observer(root)
                the_dict[key] = wrapped_value


def make_responsive(obj: object) -> object:
    """Modify object to be responsive.

    Args:
        obj (object): the object to modify

    Returns:
        Modified object.
    """
    wrapped_value = DictWrapper(obj)
    __apply_wrapper(wrapped_value, None)
    return wrapped_value
