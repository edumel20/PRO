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

- **sphere-volume**
```python
def run(radius: float) -> float:
    PI_NUMBER = 3.14
    volume = (4/3) * PI_NUMBER * radius**3
    return volume
```

- **triangle-area**
```python
def run(base: float, height: float) -> float:
    area = (1/2) * base * height
    return area
```

- **interest-rate**
```python
def run(amount: float, rate: float, years: int) -> float:
    future_amount = amount * (1 + rate / 100)**years
    return future_amount
```

- **euclid-distance**
```python
def run(x1: float, y1: float, x2: float, y2: float) -> float:
    p1_position = (x2 - x1)**2
    p2_position = (y2- y1)**2

    distance = (p1_position + p2_position) ** 0.5 
    return distance
```

- **century-year**
```python
def run(year: int) -> int:
    century = (year + 99) // 100
    return century
```

- **red-square**
```python

```
