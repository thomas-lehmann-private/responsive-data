"""Module wrapper.

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
from typing import Any

from responsive.constants import Context, Operation
from responsive.observer import Observer
from responsive.subject import Subject


class DictWrapper(Subject, Observer):
    """Wrapper for a dictionary object.

    Example:

        >>> from responsive.observer import DefaultObserver
        >>> observer = DefaultObserver()
        >>> book = DictWrapper({"author": "", "title": ""})
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
                if isinstance(value, list):
                    self.obj[name].replace(value)
                else:
                    old_value = self.obj[name]
                    self.obj[name] = value
                    self.notify(
                        id=id(self),
                        context=Context.DICTIONARY,
                        name=name,
                        old=old_value,
                        new=value,
                        operation=Operation.VALUE_CHANGED,
                    )
            else:
                old_value = self.obj.__dict__[name]
                self.obj.__dict__[name] = value
                self.notify(
                    id=id(self),
                    context=Context.CLASS,
                    name=name,
                    old=old_value,
                    new=value,
                    operation=Operation.VALUE_CHANGED,
                )
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


class ListWrapper(Subject, Observer):
    """Wrapper for a dictionary object."""

    def __init__(self, obj: object):
        """Initialize wrapper.

        Args:
            obj (objec): object to wrap.
        """
        super().__init__()
        self.obj = obj

    def append(self, value):
        """Appending a value to the list."""
        self.obj.append(value)
        self.notify(id=id(self), context=Context.LIST, new=value, operation=Operation.VALUE_ADDED)

    def remove(self, value):
        """Removing a value to the list."""
        self.obj.remove(value)
        self.notify(id=id(self), context=Context.LIST, old=value, operation=Operation.VALUE_REMOVED)

    def __setitem__(self, index, value):
        """Change value at given index."""
        old_value = self.obj[index]
        self.obj[index] = value
        self.notify(
            id=id(self),
            context=Context.LIST,
            index=index,
            old=old_value,
            new=value,
            operation=Operation.VALUE_CHANGED,
        )

    def __getitem__(self, index):
        """Get value at given index."""
        return self.obj[index]

    def replace(self, obj):
        """Replacing content."""
        if isinstance(obj, list):
            self.obj = obj
            self.notify(id=id(self), context=Context.LIST, operation=Operation.VALUE_CHANGED)

    def update(self, subject: object, *args: Any, **kwargs: Any):
        """Called when related subject has changed.

        Args:
            subject (object): the one who does the notification.
            *args (Any): optional positional arguments
            **kwargs (Any): optional key/value arguments
        """
        self.notify(*args, **kwargs)

    def __eq__(self, other: object) -> bool:
        """Comparing two lists.

        Args:
            other (object): another object to compare with

        Returns:
            true when equal, otherwise false.
        """
        if isinstance(other, list):
            return self.obj.__eq__(other)

        if isinstance(other, ListWrapper):
            return self.obj.__eq__(other.obj)

        return False
