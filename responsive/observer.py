""" Module observer.

..
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


class Observer:
    """Observer from the subject/observer pattern."""

    def update(self, subject: object, *args: Any, **kwargs: Any):
        """Called when related subject has changed.

        Args:
            subject (object): the one who does the notification.
            *args (Any): optional positional arguments
            **kwargs (Any): optional key/value arguments
        """
        raise NotImplementedError()


class DefaultObserver(Observer):
    """A simple observer class."""

    def __init__(self):
        """Initializing empty list of reveived updates."""
        super().__init__()
        self.__updates = []

    def update(self, subject: object, *args: Any, **kwargs: Any) -> None:
        """Called when the subject has been changed.

        Args:
            subject (object): the one who does the notification.
            *args (Any): optional positional arguments
            **kwargs (Any): optional key/value arguments
        """
        self.__updates.append((subject, args, kwargs))

    def __iter__(self):
        """Allows iterating over the updates of this observer."""
        return iter(self.__updates)

    def clear(self):
        """Delete all recently updated."""
        self.__updates.clear()

    def get_count_updates(self):
        """Provide number of updates."""
        return len(self.__updates)
