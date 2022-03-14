""" Module noxfile.

The MIT License

Copyright 2022 Thomas Lehmann.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import nox

#: Environment variables to use in each virtual environment
ENV = {"PYTHONDONTWRITEBYTECODE": "1"}

#: Python version(s) to use for testing
PYTHON_VERSIONS = ["3.10"]

#: source code locations
LOCATIONS = "responsive", "noxfile.py", "test"


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
    session.run("radon", "mi", "-s", *args, env=ENV)


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_audit(session):
    """Check vulnerations in used 3rd party libraries.

    Args:
        session(Session): nox session.
    """
    session.install("pip-audit")
    session.run("pip-audit", "-r", "requirements.txt", env=ENV)


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
        "jupyter",
    )
    session.run("mkdocs", "build", env=ENV)


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
        "--cov-report=xml",
        "--junit-xml=responsive-data-junit.xml",
        env=ENV,
    )
