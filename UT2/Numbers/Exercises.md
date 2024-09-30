- **quadratic**
```python
def run(a: int, b: int, c: int) -> tuple:
    discriminant = (b**2) - (4 * a * c)
    denominator = 2 * a
    x1 = (-b + ((discriminant) ** 0.5)) / (denominator)
    x2 = (-b - ((discriminant) ** 0.5)) / (denominator)

    return x1, x2
```

- **sin-approx**
```python
def run(x: float) -> float:
    operation = 180 - x
    numerator = (4 * x) * operation
    denominator = 40500 - (x * operation)

    sin = (numerator) / (denominator)

    return sin
```

- **circle-area**
```python
def run(radius) -> float:
    PI_NUMBER = 3.14
    area = PI_NUMBER * (radius**2)
    return area
```
