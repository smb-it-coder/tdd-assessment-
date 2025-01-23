import pytest
from src.string_calculator import add

# Test cases for various input scenarios
def test_empty_string():
    """Test for an empty string input."""
    assert add("") == 0

def test_single_number():
    """Test for a single number input."""
    assert add("1") == 1

def test_two_numbers():
    """Test for two numbers separated by a comma."""
    assert add("1,2") == 3

def test_newline_delimiter():
    """Test for newline as a delimiter."""
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    """Test for a custom delimiter."""
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    """Test for input containing negative numbers."""
    with pytest.raises(ValueError, match="Negative numbers not allowed: -1"):
        add("-1,2")

def test_multiple_negatives():
    """Test for input containing multiple negative numbers."""
    with pytest.raises(ValueError, match="Negative numbers not allowed: -1, -2"):
        add("-1,-2,3")

def test_multiple_custom_delimiters():
    """Test for multiple occurrences of a custom delimiter."""
    assert add("//|\n1|2|3") == 6

def test_invalid_number():
    """Test for invalid number input."""
    with pytest.raises(ValueError, match="Invalid input: brij"):
        add("1,brij,3")
