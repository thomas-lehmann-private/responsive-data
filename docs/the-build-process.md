# The Build Process

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
    session.run("black", *args, env=ENV)
```

 - The required package is **black** (see links at teh bottom for documentation)
 - The formatting will be done for all files and folders specified in `LOCATIONS`; 
   however you can overwrite those by specifying `--` after a session and then
   specifying the files you want (example: `nox -s use_black -- noxfile.py`)


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



## Links

 - https://nox.thea.codes/en/stable/
 - https://black.readthedocs.io/en/stable/
 - https://flake8.pycqa.org/en/latest/
 - https://pycodestyle.pycqa.org/en/latest/intro.html
 - https://bandit.readthedocs.io/en/latest/
 - https://pylint.pycqa.org/en/latest/
 - https://www.mkdocs.org
 - https://docs.pytest.org/en/7.0.x/
 - https://github.com/trailofbits/pip-audit
 - https://radon.readthedocs.io/en/latest/