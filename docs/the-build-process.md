# The Build Process

## Introduction

Please keep in mind that this are the goals:

 - ensuring that on Github and locally it is **the same build process**.
 - that the build does fail when one of the tool does fail
 - that every developer does use the build process **before** doing a commit.

## Automatic Code Formatting

Using the **nox** mechanism the function to automatically re-format
the source code is following:

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_black(session):
    """Reformat the code.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("black")
    session.run("black", "--line-length=100", *args, env=ENV)
```

 - The required package is **black** (see links at the bottom for documentation).
 - The idea is not to care about code formatting anymore.
 - The formatting will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_black -- noxfile.py`)

## Static Code Analysis with flake8

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_flake8(session):
    """Checking different code issues.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("flake8", "mccabe", "flake8-import-order", "flake8-bugbear")
    session.run(
        "flake8",
        "--max-line-length=100",
        "--enable-extensions=B,B9,BLK,C,E,F,I,W",
        "--max-complexity=8",
        *args,
        env=ENV
    )
```

 - The required package is **flake8** (see links at the bottom for documentation)
 - It's a very well known addition to the pylint tool.
 - In addition addons are installed to for checking complexity, order of imports and additional problems which are not covered by flake8 itself (see links at the bottom for documentation)
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_flake8 -- noxfile.py`)

## Static Code Analysis with pycodestyle

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_pycodestyle(session):
    """Checking code style.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("pycodestyle")
    session.run("pycodestyle", "--max-line-length=100", *args, env=ENV)
```

 - The required package is **pycodestyle** (see links at the bottom for documentation)
 - It's a very well known addition to the pylint tool.
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_pycodestyle -- noxfile.py`)

## Static Code Analysis with pylint

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_pylint(session):
    """Checking code style.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("pylint", "nox")
    session.run("pylint", "--enable-all-extensions", *args, env=ENV)
```

 - The required package is **pylint** (see links at the bottom for documentation)
 - It's the standard tool to find a bride range of issues in many different areas.
 - **Please note**: there is no config file and also there is no one wanted!
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_pylint -- noxfile.py`)

## Static Code Analysis with radon

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_radon(session):
    """Check code complexity.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("radon")
    session.run("radon", "cc", "--min=B", "--total-average", *args, env=ENV)
    session.run("radon", "mi", *args, env=ENV)
```

 - The required package is **radon** (see links at the bottom for documentation)
 - The letters "A" to "F" are used to provide a score where "A" stands for the best score meaning that the complexity is reasonable low or the maintainability is very good.
 - Method an functions with "A" are not shown for complexity
 - The "cc" is for complexity analysis while "mi" is for maintainability.
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_radon -- noxfile.py`)


## Static Code Analysis with bandit

 ```py linenums="1"
 @nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_bandit(session):
    """Checking code vulnerations.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("bandit")
    session.run("bandit", "-r", *args, env=ENV)
 ```

 - The required package is **bandit** (see links at the bottom for documentation)
 - It's a tool to find common security issues
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_bandit -- noxfile.py`)

## Static Code Analysis with pip-audit


```
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_audit(session):
    """Check vulnerations in used 3rd party libraries.

    Args:
        session(Session): nox session.
    """
    session.install("pip-audit")
    session.run("pip-audit", "-r", "requirements.txt", env=ENV)
```

 - The required package is **pip-audit** (see links at the bottom for documentation)
 - It's a tool to find issues with of the given dependencies.
 - The analysis will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_audit -- noxfile.py`)


## Generate the HTML Documentation

Using the **nox** mechanism the function to generate this HTML documentation
is following:

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_mkdocs(session):
    """Creating HTML documentation.

    Args:
        session(Session): nox session.
    """
    session.install(
        "mkdocs",
        "mkdocstrings",
        "mkdocs-material",
        "mkdocs-jupyter",
        "mkdocs-autolinks-plugin",
        "jupyter"
    )
    session.run("mkdocs", "build", env=ENV)
```

 - The installation requires some python package using `session.install`.
 - Finally the HTML is built with `session run`
 - You will then find the result in the local folder **site**.  

## Unittests and benchmarking with pytest

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_pytest(session):
    """Running unittests.

    Args:
        session(Session): nox session.
    """
    session.install("pytest", "pytest-cov", "pytest-random-order", "pytest-benchmark")
    session.install("-r", "requirements.txt")
    session.run(
        "pytest",
        "--ignore=noxfile.py",
        "--random-order",
        "--doctest-modules",
        "--cov=responsive",
        "--cov-branch",
        "--cov-fail-under=96",
        "--cov-report=term",
        "--cov-report=html",
        "--junit-xml=responsive-data-junit.xml",
        env=ENV,
    )
```

 - The required package is **pytest** (see links at the bottom for documentation).
 - Further addons are required:
    - `pytest-cov` to allow checking for code coverage.
    - `pytest-random-order` for running tests in random order.
    - `pytest-benchmark` for benchmark functions handled separately (those are not Testcases).
 - Doctests are supported.
 - A JUnit compatible XML is generate.
 - The build does fail when a test does fail or when the code coverage is below expected limit.

## Links

 - https://nox.thea.codes/en/stable/
 - https://black.readthedocs.io/en/stable/
 - https://flake8.pycqa.org/en/latest/
 - https://github.com/PyCQA/flake8-import-order
 - https://github.com/PyCQA/flake8-bugbear
 - https://pycodestyle.pycqa.org/en/latest/intro.html
 - https://bandit.readthedocs.io/en/latest/
 - https://pylint.pycqa.org/en/latest/
 - https://www.mkdocs.org
 - https://docs.pytest.org/en/7.0.x/
 - https://github.com/trailofbits/pip-audit
 - https://radon.readthedocs.io/en/latest/
 - https://docs.pytest.org/en/7.1.x/
 - https://pytest-benchmark.readthedocs.io/en/latest/
