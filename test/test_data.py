""" Module test_subject.

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
from unittest import TestCase

from responsive.data import make_responsive
from responsive.observer import DefaultObserver
from responsive.subject import Subject


class SomeOtherData:
    """Some test data."""

    def __init__(self):
        """Initialize test data."""
        self.some_str_2 = ""
        self.some_int_2 = 0
        self.some_list_2 = []


class SomeData:
    """Some test data."""

    def __init__(self):
        """Initialize test data."""
        self.some_str = ""
        self.some_int = 0
        self.some_list = []
        self.some_other_data = SomeOtherData()


class DataTest(TestCase):
    """Testing data functions."""

    def test_responsiveness(self):
        """Testing responsiveness."""
        observer = DefaultObserver()
        some_data = make_responsive(SomeData())
        some_data.add_observer(observer)

        # data changed at depth 1
        some_data.some_str = "hello world 1"
        some_data.some_int = 12345678
        some_data.some_other_data.some_str_2 = "hello world 2"
        some_data.some_other_data.some_int_2 = 87654321

        self.assertEqual(observer.get_count_updates(), 4)
        self.assertEqual(some_data.some_str, "hello world 1")
        self.assertEqual(some_data.some_int, 12345678)
        self.assertEqual(some_data.some_other_data.some_str_2, "hello world 2")
        self.assertEqual(some_data.some_other_data.some_int_2, 87654321)

        notifications = list(observer)

        self.assert_notification(
            notifications[0], some_data, (), self.create_kwargs("some_str", "", "hello world 1")
        )
        self.assert_notification(
            notifications[1], some_data, (), self.create_kwargs("some_int", 0, 12345678)
        )
        self.assert_notification(
            notifications[2], some_data, (), self.create_kwargs("some_str_2", "", "hello world 2")
        )
        self.assert_notification(
            notifications[3], some_data, (), self.create_kwargs("some_int_2", 0, 87654321)
        )

    @staticmethod
    def create_kwargs(attribute_name: str, old_value: Any, new_value: Any) -> dict:
        """Create kwargs representing part of the notification."""
        return {"attribute_name": attribute_name, "old_value": old_value, "new_value": new_value}

    def assert_notification(self, notification: tuple, subject: Subject, args: tuple, kwargs: dict):
        """Assert notification values."""
        print(notification)
        self.assertEqual(notification[0], subject)
        self.assertEqual(notification[1], args)
        self.assertEqual(notification[2], kwargs)
