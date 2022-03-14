""" Module data.

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
from typing import Any

from responsive.subject import Subject


class Wrapper(Subject):
    """Wrapper for an object."""

    def __init__(self, obj):
        """Initialize wrapper."""
        super().__init__()
        self.obj = obj

    def __setattr__(self, name: str, value: Any) -> None:
        """Creating attribute 'obj' or changing one of its attributes."""
        if "obj" in self.__dict__:
            old_value = self.obj.__dict__[name]
            self.obj.__dict__[name] = value
            self.notify(attribute_name=name, old_value=old_value, new_value=value)
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name: str) -> Any:
        """Get value of attribute.

        Args:
            name (str): name of the attribute

        Returns:
            value of the attribute.
        """
        return self.obj.__dict__[name]


def make_responsive(obj: object) -> object:
    """Modify object to be responsive.

    Args:
        obj (object): the object to modify

    Returns:
        Modified object.
    """
    wrapped_object = Wrapper(obj)
    return wrapped_object
