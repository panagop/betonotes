---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Using Python Modules

This page demonstrates how to import and use the Python modules from the `src/betonotes` package in your Jupyter Book.

## Importing the Module

Since we've set up the project with `uv` and properly configured the package, we can import our custom modules:

```{code-cell} python
# Import the utils module from betonotes
from betonotes import utils

# Display the module location
print(f"Imported utils from: {utils.__file__}")
```

## Using the Greet Function

Let's use the `greet` function from our utils module:

```{code-cell} python
# Use the greet function
message = utils.greet("Jupyter Book User")
print(message)
```

## Using the Calculate Sum Function

Here's an example of using the `calculate_sum` function:

```{code-cell} python
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the sum
total = utils.calculate_sum(numbers)

print(f"Numbers: {numbers}")
print(f"Sum: {total}")
```

## Adding Your Own Functions

You can add more functions to `src/betonotes/utils.py` or create new modules in the `src/betonotes/` directory. Any Python code you add there will be available to import in your Jupyter Book pages!

## Example: More Complex Usage

```{code-cell} python
# You can combine multiple function calls
greetings = [utils.greet(name) for name in ["Alice", "Bob", "Charlie"]]

for greeting in greetings:
    print(greeting)

# And use them in computations
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = utils.calculate_sum(values)
print(f"\nSum of 1-10: {result}")
```

## Tips

- Keep your reusable Python code in the `src/betonotes/` directory
- Import modules at the top of your notebook pages
- You can add dependencies to `pyproject.toml` and run `uv sync` to install them
- Use docstrings in your Python code for better documentation
