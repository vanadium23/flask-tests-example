from webapp.hello.logic import format_hello


def test_hello_bob():
    assert format_hello("Bob") == "Hello Bob!"


def test_hello_number():
    assert format_hello(1) == "Hello 1!"


def test_hello_anonymous():
    assert format_hello(None) == "Hello!"
