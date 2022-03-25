"""Module noxfile.

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

#: Source code locations
LOCATIONS = "responsive", "noxfile.py", "test"

#: All the session which should run by default
nox.options.sessions = [
    "use_black",
    "use_flake8",
    "use_pycodestyle",
    "use_pylint",
    "use_bandit",
    "use_radon",
    "use_vulture",
    "use_audit",
    "use_mkdocs",
    "use_pytest",
    "create_packages",
]


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


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_flake8(session: nox.Session) -> None:
    """Checking different code issues.

    Args:
        session (nox.Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("flake8", "mccabe", "flake8-import-order", "flake8-bugbear", "flake8-colors")
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
def use_pycodestyle(session: nox.Session) -> None:
    """Checking code style.

    Args:
        session (nox.Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("pycodestyle")
    session.run("pycodestyle", "--max-line-length=100", *args, env=ENV)


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_pylint(session: nox.Session) -> None:
    """Checking code style.

    Args:
        session (nox.Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("pylint", "nox", "parameterized")
    session.run("pylint", "--enable-all-extensions", *args, env=ENV)


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
    session.run("radon", "mi", "-s", *args, env=ENV)


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_vulture(session: nox.Session) -> None:
    """Check unused code.

    Args:
        session(Session): nox session.
    """
    args = session.posargs or LOCATIONS
    session.install("vulture")
    session.run("vulture", "--exclude=noxfile.py", *args, env=ENV)


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_audit(session: nox.Session) -> None:
    """Check vulnerations in used 3rd party libraries.

    Args:
        session (nox.Session): nox session.
    """
    session.install("pip-audit")
    session.run("pip-audit", "-r", "requirements.txt", env=ENV)


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
        "jupyter",
    )
    session.run("mkdocs", "build", env=ENV)


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def use_pytest(session: nox.Session) -> None:
    """Running unittests.

    Args:
        session (nox.Session): nox session.
    """
    session.install(
        "pytest",
        "pytest-cov",
        "pytest-random-order",
        "pytest-benchmark",
        "pytest-sugar",
        "parameterized",
    )
    session.install("-r", "requirements.txt")
    session.run(
        "pytest",
        "--ignore=noxfile.py",
        "--ignore=docs/examples",
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


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def create_packages(session: nox.Session) -> None:
    """Creating packages.

    Args:
        session (nox.Session): nox session.
    """
    session.run("python", "setup.py", "sdist", "bdist_wheel")


@nox.session
@nox.parametrize("python", PYTHON_VERSIONS)
def deploy_packages(session: nox.Session) -> None:
    """Deploying packages.

    Args:
        session (nox.Session): nox session.
    """
    session.install("twine")
    session.run("twine", "upload", "--repository-url=https://test.pypi.org/legacy/", "dist/*")


@nox.session(python=False)
def clean(session: nox.Session) -> None:
    """Cleanup temporary files and folders.

    Args:
        session (nox.Session): nox session.
    """
    session.run("git", "clean", "-fdX")
