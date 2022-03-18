# Welcome to responsive-data

The basic idea of this library is to change a data to be responsive on change.
The next code should demonstrate the basic functionality: 

```py title="demo1.py"
--8<-- "demo1.py"
```
The output looks like following (you have to scroll a bit to see whole output).

```bash
subject with id 4315315648 has notified with () and {'id': 4315315648, 'context': <Context.DICTIONARY: 2>, 'name': 'some_str', 'old': 'default string', 'new': 'another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4315315648 has notified with () and {'id': 4315315648, 'context': <Context.DICTIONARY: 2>, 'name': 'some_int', 'old': 1234567890, 'new': 9876543210, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4315315648 has notified with () and {'id': 4315311712, 'context': <Context.LIST: 3>, 'new': 6, 'operation': <Operation.VALUE_ADDED: 2>}
subject with id 4315315648 has notified with () and {'id': 4315311712, 'context': <Context.LIST: 3>, 'old': 3, 'operation': <Operation.VALUE_REMOVED: 3>}
subject with id 4315315648 has notified with () and {'id': 4315311712, 'context': <Context.LIST: 3>, 'index': 2, 'old': 4, 'new': 7, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4315315648 has notified with () and {'id': 4315311712, 'context': <Context.LIST: 3>, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4315315648 has notified with () and {'id': 4315310560, 'context': <Context.DICTIONARY: 2>, 'name': 'some_other_str', 'old': 'default other string', 'new': 'yet another string', 'operation': <Operation.VALUE_CHANGED: 1>}
```

For detailed documentations please follow the links:

  - [The Subject / Observer Pattern](subject-observer.md) ([example usage](notebooks/subject-observer.ipynb))
  - [Responsive Data Handling](responsive-data-handling.md) ([example usage](notebooks/responsive-data.ipynb))
