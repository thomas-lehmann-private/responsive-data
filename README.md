# Welcome

[![build](https://github.com/thomas-lehmann-private/responsive-data/actions/workflows/build-action.yml/badge.svg)](https://github.com/thomas-lehmann-private/responsive-data/actions)
[![documentation](https://img.shields.io/badge/documentation-ok-%2300ff00)](https://thomas-lehmann-private.github.io/responsive-data)
![GitHub](https://img.shields.io/github/license/thomas-lehmann-private/responsive-data)


[![codecov](https://codecov.io/gh/thomas-lehmann-private/responsive-data/branch/main/graph/badge.svg?token=QD9X5M8ATN)](https://codecov.io/gh/thomas-lehmann-private/responsive-data)
[![CodeFactor](https://www.codefactor.io/repository/github/thomas-lehmann-private/responsive-data/badge)](https://www.codefactor.io/repository/github/thomas-lehmann-private/responsive-data)
[![CodeScene Code Health](https://codescene.io/projects/24499/status-badges/code-health)](https://codescene.io/projects/24499)
[![DeepSource](https://deepsource.io/gh/thomas-lehmann-private/responsive-data.svg/?label=active+issues&show_trend=true&token=Rk85cJy_cMVxRNsMith_Fil9)](https://deepsource.io/gh/thomas-lehmann-private/responsive-data/?ref=repository-badge)


## Requirements

 - Python installed (recommended: Python >= 3.10)
 - Installed **nox** with `pip install nox`

## Quickstart (Usage)
For basic usage of the library please read the document (see documentation badge).

```py
from responsive.data import make_responsive
from responsive.observer import OutputObserver

if __name__ == "__main__":
    subject = make_responsive(
        {
            "some_str": "string 1",
            "some_int": 1234567890,
            "some_list": [1, 2, 3, 4, 5, {"inner_str": "string 2"}],
            "some_dict": {"some_other_str": "string 3"},
        }
    )

    subject.add_observer(OutputObserver())

    # changing string field
    subject.some_str = "another string"
    # changing integer field
    subject.some_int = 9876543210
    # changing dictionary in a list
    subject.some_list[-1].inner_str = "just another string"
    # appending a value to a list field
    subject.some_list.append(6)
    # removing a value from a list field
    subject.some_list.remove(3)
    # change value by index
    subject.some_list[2] = 7
    # changing list field to another list
    subject.some_list = [5, 4, 3, 2, 1, 0]
    # changing string field of a nested dictionary
    subject.some_dict.some_other_str = "yet another string"
    # changing dictionary in total
    subject.some_dict = {"some_other_str": "string 4"}
    # changing string field of a nested dictionary (after replacement)
    subject.some_dict.some_other_str = "string 5"

```

The output looks like following:

```
subject with id 4371736816 has notified with () and {'id': 4371736816, 'context': <Context.DICTIONARY: 2>, 'name': 'some_str', 'old': 'string 1', 'new': 'another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371736816, 'context': <Context.DICTIONARY: 2>, 'name': 'some_int', 'old': 1234567890, 'new': 9876543210, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371739120, 'context': <Context.DICTIONARY: 2>, 'name': 'inner_str', 'old': 'string 2', 'new': 'just another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371738496, 'context': <Context.LIST: 3>, 'new': 6, 'operation': <Operation.VALUE_ADDED: 2>}
subject with id 4371736816 has notified with () and {'id': 4371738496, 'context': <Context.LIST: 3>, 'old': 3, 'operation': <Operation.VALUE_REMOVED: 3>}
subject with id 4371736816 has notified with () and {'id': 4371738496, 'context': <Context.LIST: 3>, 'index': 2, 'old': 4, 'new': 7, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371736816, 'context': <Context.DICTIONARY: 2>, 'name': 'some_list', 'old': [1, 2, 7, 5, {'inner_str': 'just another string'}, 6], 'new': [5, 4, 3, 2, 1, 0], 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371737344, 'context': <Context.DICTIONARY: 2>, 'name': 'some_other_str', 'old': 'string 3', 'new': 'yet another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371736816, 'context': <Context.DICTIONARY: 2>, 'name': 'some_dict', 'old': {'some_other_str': 'yet another string'}, 'new': {'some_other_str': 'string 4'}, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4371736816 has notified with () and {'id': 4371738496, 'context': <Context.DICTIONARY: 2>, 'name': 'some_other_str', 'old': 'string 4', 'new': 'string 5', 'operation': <Operation.VALUE_CHANGED: 1>}
```

## Quickstart (Build)

```
nox
```

 ## Interesting Links

  - https://test.pypi.org/project/responsive-data/

