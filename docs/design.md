# The design

## Introduction

Please note that there are further links on the left side. This article is basically
about how it works.

## The wrapper concept

The wrapper is required to implement a mechanism that is aware of changes. There are currently two wrappers: one for a dictionary or a class and another one for lists.

```py
wrapped_dict = DictWrapper({"name": ""})
wrapped_dict.name = "Raymond Chandler"
print(wrapped_dict.name)

wrapped_list = ListWrapper([1, 2, 3, 4])
wrapped_list.append(5)
wrapped_list[0] = 10
print(wrapped_list[2])
```

Basically the wrapper have to implement a few methods otherwise those statements would fail.

| Wrapper class  | Method to overload | Meaning                               |
| -------------- | ------------------ | ------------------------------------- |
| DictWrapper    | `__setattr__`      | set value for an attribute (name)     |
|                | `__getattr__`      | get value for an attribute (name)     |
|                | `__repr__`         | string representation of object       |
|                | `update`           | a wrapper is subject **and** observer |
| ListWrapper    | `__setitem__`      | set value at given index              |
|                | `__getitem__`      | get value at given index              |
|                | `__repr__`         | string representation of object       |
|                | `append`           | appending a value to list             |
|                | `remove`           | removing value from list              |
|                | `update`           | a wrapper is subject **and** observer |

Another important aspect of the dictionary wrapping is the capability to have access to the individual fields by using the dot. As you probably remember as well the dictionary doesn't allow this; instead you have to do it this way:

```py
data = {"name": "Raymond Chandler"}
print(data["name"])
```

Of course you shouldn't use the wrappers directly since they are implementation details of the library. The way to go:

```py title="demo2.py"
--8<-- "demo2.py"
```

The injecting of the wrappers is done for the root object and recursively for all values which are either a dictionary, a list or a class (exception: for the moment the values of the list are ignored)

## The responsiveness

### Subject/Observer pattern

The responsiveness requires implementing a mechanism which does a notification on change. The library does use the subject/observer design pattern.

A **subject** is data which can be changed and should do (automatically) a notification on change. An **observer** is an object interested in changes and will be registered at the subject. When a change does happen each registered observer will be notified.

All objects returns by **make_responsive** are basically subjects.

```py title="demo3.py"
--8<-- "demo3.py"
```
The output looks like this one:

```
title=The Big Sleep, author=[]
title=The Big Sleep, author=['Raymond Chandler']
```

### Define observer interests

You have the control to decide when an observer will be notified. The default is to get notified on each change but you can override the `get_interests` method to change the filter. The next snippets defines a method where you implement a dictionary that can have multiple fields (that should exist) and the value is a function where you define for which value of the related you want to have notifications.

```py
    def get_interests(self) -> dict[str, Callable[[Any], bool]]::
        """Get notifications when the title has changed for any value."""
        return {"title": lambda value: True}
```

This one filters on both (name of the field and value):

```py
    def get_interests(self) -> dict[str, Callable[[Any], bool]]::
        """Get notifications when the author has changed to concrete value  ."""
        return {"author": lambda value: value == "Raymond Chandler"}
```
