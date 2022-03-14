# How to write performance test

It's really easy. The **pytest** session includes the plugin **pytest-benchmark**.
With this writing a performance test is simply writing functions like following:

```py linenums="1"
def test_subject_observer_performance(benchmark):
    """Testing simple notification process with many observers."""
    observers = [DefaultTestObserver() for _ in range(1000000)]
    subject = Subject()

    for observer in observers:
        subject.add_observer(observer)

    benchmark(subject.notify)
```

The example here does 1000000 attaching of observers to one subject;
the notification part is the call that will be measured. You simply
define a function with one parameter **benchmark** which will be
a function that you can use to pass another function and its parameters.
In given example we didn't pass parameters.

![](performance-results.png)

For more details please read here: https://pytest-benchmark.readthedocs.io/en/latest/.
