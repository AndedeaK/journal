import pytest

from journal import make_entry, check_cmdline, view_entry, greet, interact, interact1


def test_check_cmdline():
    with pytest.raises(SystemExit):
        check_cmdline()


def test_greet():
    with pytest.raises(TypeError):
        greet(1)

def test_interact():
    with pytest.raises(TypeError):
        interact(1)

def test_interact1():
    with pytest.raises(TypeError):
        interact1(1)


def test_make_entry():
    with pytest.raises(TypeError):
        make_entry(1)
    with pytest.raises(ValueError):
        make_entry("123456789")


def test_view_entry():
    with pytest.raises(FileNotFoundError):
        view_entry("page.txt")
