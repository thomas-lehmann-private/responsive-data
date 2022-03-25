# Welcome to responsive-data

The basic idea of this library is to change a data to be responsive on change.
The next code should demonstrate the basic functionality: 

```py title="demo1.py"
--8<-- "demo1.py"
```
The output looks like following (you have to scroll a bit to see whole output).

```bash
subject with id 4309460944 has notified with () and {'id': 4309460944, 'context': <Context.DICTIONARY: 2>, 'name': 'some_str', 'old': 'string 1', 'new': 'another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4309460944 has notified with () and {'id': 4309460944, 'context': <Context.DICTIONARY: 2>, 'name': 'some_int', 'old': 1234567890, 'new': 9876543210, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4309460944 has notified with () and {'id': 4309463248, 'context': <Context.DICTIONARY: 2>, 'name': 'inner_str', 'old': 'string 2', 'new': 'just another string', 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4309460944 has notified with () and {'id': 4309461616, 'context': <Context.LIST: 3>, 'new': 6, 'operation': <Operation.VALUE_ADDED: 2>}
subject with id 4309460944 has notified with () and {'id': 4309461616, 'context': <Context.LIST: 3>, 'old': 3, 'operation': <Operation.VALUE_REMOVED: 3>}
subject with id 4309460944 has notified with () and {'id': 4309461616, 'context': <Context.LIST: 3>, 'index': 2, 'old': 4, 'new': 7, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4309460944 has notified with () and {'id': 4309461616, 'context': <Context.LIST: 3>, 'operation': <Operation.VALUE_CHANGED: 1>}
subject with id 4309460944 has notified with () and {'id': 4309453936, 'context': <Context.DICTIONARY: 2>, 'name': 'some_other_str', 'old': 'string 3', 'new': 'yet another string', 'operation': <Operation.VALUE_CHANGED: 1>}
```

For detailed documentations please follow the links:

  - [The Subject / Observer Pattern](subject-observer.md) ([example usage](notebooks/subject-observer.ipynb))
  - [Responsive Data Handling](responsive-data-handling.md) ([example usage](notebooks/responsive-data.ipynb))
