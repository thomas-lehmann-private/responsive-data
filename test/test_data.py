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
from test.observers import DefaultTestObserver
from unittest import TestCase

from responsive.data import make_responsive


class SomeData:
    """Some test data."""

    def __init__(self):
        """Initialize test data."""
        self.some_str = ""
        self.some_int = 0
        self.some_list = []


class DataTest(TestCase):
    """Testing data functions."""

    def test_responsiveness(self):
        """Testing responsiveness."""
        observer = DefaultTestObserver()
        some_data = make_responsive(SomeData())
        some_data.add_observer(observer)

        # data changed at depth 1
        some_data.some_str = "hello world 1"
        some_data.some_int = 12345678

        self.assertEqual(observer.get_count_notifications(), 2)
        self.assertEqual(some_data.some_str, "hello world 1")
        self.assertEqual(some_data.some_int, 12345678)

        notifications = list(observer.get_notifications())

        self.assertEqual(notifications[0][0], some_data)
        self.assertEqual(notifications[0][1], ())
        self.assertDictEqual(
            notifications[0][2],
            {
                "attribute_name": "some_str",
                "old_value": "",
                "new_value": "hello world 1",
            },
        )

        self.assertEqual(notifications[1][0], some_data)
        self.assertEqual(notifications[1][1], ())
        self.assertDictEqual(
            notifications[1][2],
            {
                "attribute_name": "some_int",
                "old_value": 0,
                "new_value": 12345678,
            },
        )
