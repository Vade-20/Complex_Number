# Complex Number Class

This is a Python class that represents complex numbers. It provides various operations such as addition, subtraction, multiplication, and division on complex numbers. The class also includes methods to check if a given string represents a valid complex number.It take string as an argument.

## Usage

To use the `Complex` class, follow these steps:

1. Import the required modules:
   ```python
   import re
   from fractions import Fraction
   ```

2. Create an instance of the `Complex` class by passing a string representing a complex number to the constructor:
   ```python
   complex_number = Complex("3+4i")
   ```

3. Perform operations on complex numbers using the available methods. For example:
   ```python
   complex_number_1 = Complex("3+4i")
   complex_number_2 = Complex("2-1i")

   # Addition
   result = complex_number_1 + complex_number_2

   # Subtraction
   result = complex_number_1 - complex_number_2

   # Multiplication
   result = complex_number_1 * complex_number_2

   # Division
   result = complex_number_1 / complex_number_2
   ```

4. Display the complex number using the `str` method or by accessing the `complex_number` property:
   ```python
   print(complex_number)  # Output: 3+4i

   # Accessing individual components
   print(complex_number.real)  # Output: 3
   print(complex_number.imag)  # Output: 4i
   ```

## Class Methods

The `Complex` class provides the following methods:

- `__init__(self, complex_number: str)`: Initializes a complex number object based on the provided string representation.
- `iscomplex(self)`: Checks if the complex number is valid.
- `__add__(self, second)`: Performs addition of two complex numbers.
- `__sub__(self, second)`: Performs subtraction of two complex numbers.
- `__mul__(self, second)`: Performs multiplication of two complex numbers.
- `__truediv__(self, second)`: Performs division of two complex numbers.
- `__str__(self) -> str`: Returns a string representation of the complex number.

## Properties

The `Complex` class provides the following properties:

- `complex_number`: Returns the formatted string representation of the complex number.
- `real`: Returns the real component of the complex number as a `Fraction` object.
- `imag`: Returns the imaginary component of the complex number as a string.

## Example

Here's an example usage of the `Complex` class:

```python
# Create a complex number object
complex_number = Complex("3+4i")

# Perform operations
complex_number_2 = Complex("2-1i")
result = complex_number + complex_number_2

# Display the result
print(result)  # Output: 5+3i
```

Please note that the provided string must represent a valid complex number for the operations to work correctly.
