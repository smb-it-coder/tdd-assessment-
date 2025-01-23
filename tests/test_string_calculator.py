import pytest
from src.string_calculator import add

class TestStringCalculator:
    
    def test_empty_string(self):
        """Test for an empty string input."""
        assert add("") == 0

    def test_single_number(self):
        """Test for a single number input."""
        assert add("1") == 1

    def test_two_numbers(self):
        """Test for two numbers separated by a comma."""
        assert add("1,2") == 3

    def test_newline_delimiter(self):
        """Test for newline as a delimiter."""
        assert add("1\n2,3") == 6

    def test_custom_delimiter(self):
        """Test for a custom delimiter."""
        assert add("//;\n1;2") == 3

    def test_negative_numbers(self):
        """Test for input containing negative numbers."""
        with pytest.raises(ValueError, match="Negative numbers not allowed: -1"):
            add("-1,2")

    def test_multiple_negatives(self):
        """Test for input containing multiple negative numbers."""
        with pytest.raises(ValueError, match="Negative numbers not allowed: -1, -2"):
            add("-1,-2,3")

    def test_multiple_custom_delimiters(self):
        """Test for multiple occurrences of a custom delimiter."""
        assert add("//|\n1|2|3") == 6

    def test_invalid_number(self):
        """Test for invalid number input."""
        with pytest.raises(ValueError, match="Invalid input: brij"):
            add("1,brij,3")
