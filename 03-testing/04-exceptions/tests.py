from book import Book
import pytest

@pytest.mark.parametrize("title", [
    "",
    None
])
def test_invalid_title(title):
    with pytest.raises(ValueError):
        assert Book(title, "978-1779501127")

@pytest.mark.parametrize("title", [
    "hello pietpiraat",
    "bumba in het circus"
])
def test_valid_title(title):
    assert Book(title, "978-1779501127")

@pytest.mark.parametrize("isbn",[
    "978-17795011"
    "978-1234567890"
])
def test_invalid_isbn(isbn):
    with pytest.raises(ValueError):
        assert Book("bumba in het circus", isbn)

