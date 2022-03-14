""" Module observers.

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

from responsive.observer import Observer
from responsive.subject import Subject


class DefaultTestObserver(Observer):
    """Test observer class."""

    def __init__(self):
        """initialize empty notification list."""
        self.__notifications = []

    def update(self, subject: Subject, *args: Any, **kwargs: Any):
        """Called when subject does notify."""
        self.__notifications.append((subject, args, kwargs))

    def get_count_notifications(self):
        """Get count of notifications"""
        return len(self.__notifications)

    def get_notifications(self):
        """Get notifications."""
        return iter(self.__notifications)
