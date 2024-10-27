- **leap-year**
```python
def run(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
    return is_leap_year
```

- **marvel-akinator**
```python

```

- **simple-op**
```python
def run(num1: int, num2: int, op: str) -> float:
    match op:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case _:
            result = None
    return result
```

- **rps**
```python

```

- **min3values**
```python
def run(value1: int | float, value2: int | float, value3: int | float) -> int | float:
    
    if value1 < value2 and value1 < value3:
        min_value = value1
    elif value2 < value1 and value2 < value3:
        min_value = value2
    elif value3 < value1 and value3 < value2:
        min_value = value3
    else:
        min_value = value1
    return min_value
```

- **blood-donation**
```python
def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    suitable_age = 18 <= age <= 65
    suitable_weight = weight > 50
    suitable_heartbeat = 50 <= heartbeat <= 110
    suitable_platelets = platelets >= 150_000

    if suitable_age and suitable_weight and suitable_heartbeat and suitable_platelets:
        suitable_for_donation = True
    else:
        suitable_for_donation = False

    return suitable_for_donation
```

- **facemoji**
````python
def run(feeling: str) -> str:
    match feeling.lower():
        case 'happy':
            emoji = '😀'
        case 'sad':
            emoji = '😔'
        case 'angry':
            emoji = '😡'
        case 'pensive':
            emoji = '🤔'
        case 'surprised':
            emoji = '😮'
        case _:
            emoji = None
    return emoji
```
