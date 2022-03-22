"""Demo code."""
from responsive.data import make_responsive

book = make_responsive({
    "title": "The Big Sleep",
    "authors": ["Raymond Chandler"]
})

print(book.title)
print(book.authors[0])
