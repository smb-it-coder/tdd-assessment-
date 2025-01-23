import re

class StringCalculator:
    def __init__(self):
        self.delimiters = [',', '\n']

    def add(self, numbers: str) -> int:
        """
        A String Calculator to calculate the sum of numbers in a string.

        Args:
            numbers (str): A string of numbers separated by a delimiter.

        Returns:
            int: The sum of the numbers.

        Raises:
            ValueError: If negative numbers are present.
        """
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            match = re.match(r"//(.+)\n(.*)", numbers)
            if match:
                custom_delimiter, numbers = match.groups()
                self.delimiters.append(re.escape(custom_delimiter))

        # Create the delimiter pattern
        delimiter_pattern = '|'.join(self.delimiters)

        # Split the string by delimiters
        number_list = re.split(delimiter_pattern, numbers)

        # Convert to integers and validate
        integers = []
        negatives = []
        for num in number_list:
            if num:
                try:
                    n = int(num)
                    if n < 0:
                        negatives.append(n)
                    integers.append(n)
                except ValueError:
                    raise ValueError(f"Invalid input: {num}")

        # Raise exception for negative numbers
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return sum(integers)
