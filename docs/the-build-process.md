# The Build Process

## Introduction

Please keep in mind that this are the goals:

 - ensuring that on Github and locally it is **the same build process**.
 - that the build does fail when one of the tool does fail
 - that every developer does use the build process **before** doing a commit.

## Default sessions

```py linenums="1"
#: All the session which should run by default
nox.options.sessions = [
    "use_black",
    "use_flake8",
    "use_pycodestyle",
    "use_pylint",
    "use_bandit",
    "use_radon",
    "use_audit",
    "use_mkdocs",
    "use_pytest",
    "create_packages",
```

The main reason for this is that the deploying of the packages is done only
when intending to deploy a release. The only way to exclude that session is
to define which sessions should run by default when executing `nox`.

## Automatic Code Formatting

Using the **nox** mechanism the function to automatically re-format
the source code is following:

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_black(session: nox.Session) -> None:
    """Reformat the code.

    Args:
        session (nox.Session): nox session.
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
def use_flake8(session: nox.Session) -> None:
    """Checking different code issues.

    Args:
        session (nox.Session): nox session.
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
def use_pycodestyle(session: nox.Session) -> None:
    """Checking code style.

    Args:
        session (nox.Session): nox session.
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
def use_pylint(session: nox.Session) -> None:
    """Checking code style.

    Args:
        session (nox.Session): nox session.
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
def use_radon(session: nox.Session) -> None:
    """Check code complexity.

    Args:
        session (nox.Session): nox session.
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
def use_bandit(session: nox.Session) -> None:
    """Checking code vulnerations.

    Args:
        session (nox.Session): nox session.
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
def use_audit(session: nox.Session) -> None:
    """Check vulnerations in used 3rd party libraries.

    Args:
        session (nox.Session): nox session.
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
def use_mkdocs(session: nox.Session) -> None:
    """Creating HTML documentation.

    Args:
        session (nox.Session): nox session.
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
def use_pytest(session: nox.Session) -> None:
    """Running unittests.

    Args:
        session (nox.Session): nox session.
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

## Creating the packages

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def create_packages(session: nox.Session) -> None:
    """Creating packages.

    Args:
        session (nox.Session): nox session.
    """
    session.run("python", "setup.py", "sdist", "bdist_wheel")
```

 - with **sdist** you generate the source package.
 - with **bdist_wheel** you generate the binary package ensuring all dependencies are installed too (when given).
 - you will find the packages in folder **dist**.

## Deploying the packages

```py linenums="1"
@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def deploy_packages(session: nox.Session) -> None:
    """Deploying packages.

    Args:
        session (nox.Session): nox session.
    """
    session.install("twine")
    session.run("twine", "upload", "--repository-url=https://test.pypi.org/legacy/", "dist/*")
```

 - the given setup does upload the packages to the PYPI test instance (will be changed later on)
 - you have to ensure that the environment variables **TWINE_USERNAME** and **TWINE_PASSWORD** are set accordingly;
   the username is the name of the token you have specified in the PYPI instance and the password is the token
   that has been generated by the PYPI instance for you.
 - those variables have to be set into the secrets section of the repository at Github that the Github action are
   able to inject them into the build process.

## Cleanup

```py linenums="1"
@nox.session(python=False)
def clean(session: nox.Session) -> None:
    """Cleanup temporary files and folders.

    Args:
        session (nox.Session): nox session.
    """
    session.run("git", "clean", "-fdX")
```

 - Using git it is very easy to remove all temporary files and folders.
 - The **X** is necessary to include the files and folders defined in `.gitignore`
 - The `python=False` disables the creation of a virtual environment.
 - Of course the **clean** session is not in the list of the default sessions.

## Links

### The build tool itself
 - https://nox.thea.codes/en/stable/

### Code formatting
 - https://black.readthedocs.io/en/stable/


### Static code analysis
 - https://flake8.pycqa.org/en/latest/
 - https://github.com/PyCQA/flake8-import-order
 - https://github.com/PyCQA/flake8-bugbear
 - https://pycodestyle.pycqa.org/en/latest/intro.html
 - https://bandit.readthedocs.io/en/latest/
 - https://pylint.pycqa.org/en/latest/
 - https://github.com/trailofbits/pip-audit
 - https://radon.readthedocs.io/en/latest/

### Documentation
 - https://www.mkdocs.org

### Unittesting and Benchmarking
 - https://docs.pytest.org/en/7.1.x/
 - https://pytest-benchmark.readthedocs.io/en/latest/


### Packages and Deployment
 - https://packaging.python.org/en/latest/tutorials/packaging-projects/
 - https://realpython.com/pypi-publish-python-package/
