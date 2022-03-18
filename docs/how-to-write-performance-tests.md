# How to write performance test

It's really easy. The **pytest** session includes the plugin **pytest-benchmark**.
With this writing a performance test is simply writing functions like following:

```py linenums="1"
def test_subject_with_one_observer_with_special_interest_performance(benchmark):
    """Testing advanced notification mechanism."""
    observer = DefaultObserver()
    observer.set_interests(
        {"value": lambda value: value % 2 == 0}  # pylint: disable=compare-to-zero
    )
    subject = Subject()
    subject.add_observer(observer)

    def func():
        subject.notify(value=2)

    benchmark(func)
```

The example here does attaching of one observer with special interest to one subject;
the notification part is the call that will be measured. You simply
define a function passing it to the  **benchmark** function.

It's important that you write those tests for small scenarios since the scaling
is automatically tested by the bechmark framework.

![](performance-results.png)

For more details please read here: https://pytest-benchmark.readthedocs.io/en/latest/.
