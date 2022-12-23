import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("../assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_parse_template_multiword():
    actual_stripped, actual_parts = parse_template(
        "It was a {Plural Noun} and {First Name} {Number from 1-50}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Plural Noun", "First Name", "Number from 1-50")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


# test that empty strings are converted to 'blank'
def test_merge_blanks():
    actual = merge("It was a {} and {} {}.", ("", "", ""))
    expected = "It was a blank and blank blank."
    assert actual == expected


# test that number inputs are properly merged
def test_merge_numbers():
    actual = merge("It was a {} and {} {}.", (3, 4, 5))
    expected = "It was a 3 and 4 5."
    assert actual == expected


# test that symbol inputs are properly merged
def test_merge_symbols():
    actual = merge("It was a {} and {} {}.", ('%', '$', '&'))
    expected = "It was a % and $ &."
    assert actual == expected


def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
