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

from responsive.observer import Observer
from responsive.subject import Subject


class Wrapper(Subject, Observer):
    """Wrapper for an object.

    Example:

        >>> from responsive.observer import DefaultObserver
        >>> observer = DefaultObserver()
        >>> book = Wrapper({"author": "", "title": ""})
        >>> book.add_observer(observer)
        >>> book.author = "Raymond Chandler"
        >>> book.title = "The Big Sleep"
        >>> observer.get_count_updates()
        2
    """

    def __init__(self, obj: object):
        """Initialize wrapper.

        Args:
            obj (objec): object to wrap.
        """
        super().__init__()
        self.obj = obj

    def __repr__(self) -> str:
        """Get string representation of wrapped data.

        Returns:
            string representation of wrapped data.
        """
        return f"{self.obj}"

    def __setattr__(self, name: str, value: Any) -> None:
        """Creating attribute 'obj' or changing one of its attributes.

        Args:
            name  (str): name of the attribute.
            value (Any): value of the attribute.
        """
        if "obj" in self.__dict__:
            if isinstance(self.obj, dict):
                old_value = self.obj[name]
                self.obj[name] = value
                self.notify(attribute_name=name, old_value=old_value, new_value=value)
            else:
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
        if isinstance(self.obj, dict):
            return self.obj[name]

        return self.obj.__dict__[name]

    def update(self, subject: object, *args: Any, **kwargs: Any):
        """Called when related subject has changed.

        Args:
            subject (object): the one who does the notification.
            *args (Any): optional positional arguments
            **kwargs (Any): optional key/value arguments
        """
        self.notify(*args, **kwargs)


def __apply_wrapper(root: object, parent: object) -> None:
    """Modify recursive object to be responsive.

    Args:
        root (object): the main object that should be responsive
        parant (object): the current parent in the hierachy (None if root)
    """
    current = parent if parent is not None else root
    the_dict = None

    if isinstance(current, Wrapper):
        __apply_wrapper(current, current.obj)
        return

    the_dict = current if isinstance(current, dict) else current.__dict__

    for key, value in the_dict.items():
        current_type = type(value)
        if str(current_type).startswith("<class"):
            if not current_type.__module__ == "builtins":
                wrapped_value = Wrapper(value)
                __apply_wrapper(root, wrapped_value)
                wrapped_value.add_observer(root)
                the_dict[key] = wrapped_value


def make_responsive(obj: object) -> object:
    """Modify object to be responsive.

    Args:
        obj (object): the object to modify

    Returns:
        Modified object.
    """
    wrapped_value = Wrapper(obj)
    __apply_wrapper(wrapped_value, None)
    return wrapped_value
