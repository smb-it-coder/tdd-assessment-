
# String Calculator TDD Kata

This repository contains an implementation of the String Calculator TDD Kata using Python. The development process follows strict TDD (Test-Driven Development) practices.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd string_calculator
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest
   ```

## Project Structure
```
TDD-ASSESSMENT/
├── src/
│   ├── __init__.py
│   └── string_calculator.py
├── tests/
│   ├── __init__.py
│   └── test_string_calculator.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Features
- Handles empty strings.
- Supports multiple delimiters.
- Throws exceptions for negative numbers.
- Adheres to TDD principles.

## How It Works
- Input strings are parsed based on specified or default delimiters.
- Numbers are summed up, throwing errors for negative values.

