from shortener import shorten_url, get_original_url


def test_shorten_url():
    original_url = "https://www.google.com"

    code = shorten_url(original_url)

    assert code is not None
    assert len(code) == 6


def test_get_original_url():
    original_url = "https://www.github.com"

    code = shorten_url(original_url)

    assert get_original_url(code) == original_url


def test_invalid_code():
    assert get_original_url("invalid123") is None