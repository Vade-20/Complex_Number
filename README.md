# Complex Number Operations

This is a Python class that allows you to perform various operations on complex numbers. It provides methods for addition, subtraction, multiplication, division, conjugate, inverse, moduli, and square root of complex numbers.

## Usage

Instantiate the `Complex` class by providing a complex number in the form of a string. The string should follow the format `a+bi`, where `a` is the real part and `b` is the imaginary part. The following operations are supported:

### Addition

To add two complex numbers `c1` and `c2`, use the `+` operator:

```python
result = c1 + c2
```

### Subtraction

To subtract one complex number `c2` from another complex number `c1`, use the `-` operator:

```python
result = c1 - c2
```

### Multiplication

To multiply two complex numbers `c1` and `c2`, use the `*` operator:

```python
result = c1 * c2
```

### Division

To divide one complex number `c1` by another complex number `c2`, use the `/` operator:

```python
result = c1 / c2
```

### Conjugate

To calculate the conjugate of a complex number `c`, use the `conjugate()` method:

```python
result = c.conjugate()
```

### Inverse

To calculate the inverse of a complex number `c`, use the `inverse()` method:

```python
result = c.inverse()
```

### moduli

To calculate the moduli of a complex number `c`, use the `moduli()` method:

```python
result = c.moduli()
```

### Square Root

To calculate the square root of a complex number `c`, use the `sqrt_complex()` method:

```python
result = c.sqrt_complex()
```

### String Representation

To obtain a string representation of a complex number `c`, use the `str()` function or simply print the object:

```python
print(c)
```

## Example

Here's an example demonstrating the usage of the `Complex` class:

```python
# Create complex numbers
c1 = Complex("3+2i")
c2 = Complex("1-4i")

# Perform operations
addition = c1 + c2
subtraction = c1 - c2
multiplication = c1 * c2
division = c1 / c2
conjugate = c1.conjugate()
inverse = c1.inverse()
moduli = c1.moduli()
sqrt_complex = c1.sqrt_complex()

# Print results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Conjugate:", conjugate)
print("Inverse:", inverse)
print("moduli:", moduli)
print("Square Root:", sqrt_complex)
```

## Note

The input complex numbers should be in the form `a+bi` or `bi+a`, where `a` and `b` are real numbers. Make sure to provide valid complex numbers to avoid exceptions.