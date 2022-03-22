"""Demo code."""
from typing import Any

from responsive.data import make_responsive
from responsive.observer import Observer
from responsive.subject import Subject


class BookObserver(Observer):
    """A simple book observer."""

    def update(self, book: Subject, *args: Any, **kwargs: Any) -> None:
        """Simple notification from the subject."""
        print(f"title={book.title}, author={book.authors}")


if __name__ == "__main__":
    observer = BookObserver()
    book = make_responsive({"title": "", "authors": []})
    book.add_observer(observer)

    book.title = "The Big Sleep"
    book.authors.append("Raymond Chandler")
