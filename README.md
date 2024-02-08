# F-Strings

## Aligning and Filling the Output

- `<` - Aligns the interpolated value to the left within the available space. It’s the default alignment for most objects.
- `>` - Aligns the interpolated value to the right within the available space. It’s the default alignment for numbers.  
- `^` -  Aligns the interpolated value in the center of the available space.  
- `=` - Adds padding after the sign but before the digits in numeric values. It’s the default for numbers when 0 immediately precedes the field width. 


```python
text = "Hello!"

# width=30
f"{text:30}"
'Hello!                        '

# align="<" and width=30
f"{text:<30}"
'Hello!                        '

# align="^" and width=30
f"{text:^30}"
'            Hello!            '

# align=">" and width=30
f"{text:>30}"
'                        Hello!'

# fill="=", align="^" and width=30
f"{text:=^30}"
'============Hello!============'
```


## Converting Between Type Representations


- `b`	Binary	Converts the number to base 2
- `c`	Character	Converts the number to the corresponding Unicode character
- `d`	Decimal Integer	Converts the number to base 10
- `o`	Octal	Converts the number to base 8
- `x` or `X`	Hexadecimal	Converts the number to base 16, using lowercase or uppercase letters for the digits above 9
- `n`	Number	Works the same as d, except that it uses the current locale setting to insert the appropriate thousand separator characters
- `None`	Decimal Integer	Works the same as d

```python
number = 42

f"int: {number:d},  hex: {number:x},  oct: {number:o},  bin: {number:b}"
'int: 42,  hex: 2a,  oct: 52,  bin: 101010'
```

- `e` or `E`	Scientific notation with the separator character in lowercase or uppercase, respectively
- `f` or `F`	Fixed-point notation with nan and inf in lowercase or in uppercase, respectively
- `g` or `G`	General format where small numbers are represented in fixed-point notation and larger numbers in scientific notation
- `n`	General format (same as g), except that it uses a locale-aware character as a thousand separator


```python
large = 1234567890

f"{large:e}"
'1.234568e+09'
f"{large:E}"
'1.234568E+09'

number = 42.42

f"{number:f}"
'42.420000'

inf = float("inf")

f"{inf:f}"
'inf'
f"{inf:F}"
'INF'

f"{large:g}"
'1.23457e+09'
f"{large:G}"
'1.23457E+09'
f"{number:g}"
'42.42'
```

## Formatting Numeric Values to Improve Presentation

```python
from math import pi

pi
3.141592653589793

f"{pi:.4f}"
'3.1416'

f"{pi:.8f}"
'3.14159265'
```

- `,` -	Allows you to use a comma as a thousand separator
- `_` -	Allows you to use an underscore as a thousand separator

```python
number = 1234567890

f"{number:,}"
'1,234,567,890'

f"{number:_}"
'1_234_567_890'

f"{number:,.2f}"
'1,234,567,890.00'

f"{number:_.2f}"
'1_234_567_890.00'
```

## Adding Signs

- `+` - Indicates that a sign should be used for both positive and negative numbers
- `-` -	Indicates that a sign should be used only for negative numbers, which is the default behavior
- `space` - Indicates that a leading space should be used on positive numbers and a minus sign on negative numbers

```python
positive = 42
negative = -42

f"{positive:+}"
'+42'
f"{negative:+}"
'-42'

f"{positive:-}"
'42'
f"{negative:-}"
'-42'

f"{positive: }"
' 42'
f"{negative: }"
'-42'
```

## Providing Formatting Fields Dynamically

```python
total = 123456.99

# Formatting values
width = 30
align = ">"
fill = "."
precision = 2
sep = ","

f"Total{total:{fill}{align}{width}{sep}.{precision}f}"
'Total....................123,456.99'
```

## Representing Currency Values

```python
>>> inventory = [
...     {"product": "Apple", "price": 5.70},
...     {"product": "Orange", "price": 4.50},
...     {"product": "Banana", "price": 6.00},
...     {"product": "Mango", "price": 8.60},
...     {"product": "Pepper", "price": 4.20},
...     {"product": "Carrot", "price": 3.57},
... ]

>>> for item in inventory:
...     product = item["product"]
...     price = item["price"]
...     print(f"{product:.<30}${price:.2f}")
...
Apple.........................$5.70
Orange........................$4.50
Banana........................$6.00
Mango.........................$8.60
Pepper........................$4.20
Carrot........................$3.57
```


## Formatting Dates

```python
>>> from datetime import datetime

>>> now = datetime.now()
>>> now
datetime.datetime(2024, 1, 31, 14, 6, 53, 251170)

>>> >>> f"Today is {now:%a %b %d, %Y} and it's {now:%H:%M} hours"
"Today is Wed Jan 31, 2024 and it's 14:06 hours"
```

## Expressing Percentages

The `%` modifier allows you to express a number as a percentage. Under the hood, this modifier multiplies the number by 100, displays it in fixed-point notation, and adds a percent sign at the end.
```python
wins = 25
games = 35

f"Team's winning percentage: {wins / games:.2%}"

"Team's winning percentage: 71.43%"
```


## Result of Using "#"

- `int` - Adds the prefix 0b, 0o, 0x, or 0X to binary, octal, hexadecimal, and capital-hexadecimal notations, respectively
- `float` and `complex` - Adds the decimal-point character to the end of the value even if no digit follows it

```python
number = 42

f"hex: {number:#x};  oct: {number:#o};  bin: {number:#b}"
'hex: 0x2a;  oct: 0o52;  bin: 0b101010'

f"float: {number:#.0f}"
'float: 42.'
```

In the first example, you use different integer variations to represent a number. The `#` specifier adds the appropriate prefix to the output.

In the second example, you represent a number as a floating-point value. In this case, you have a precision of 0, meaning that you don’t want to display decimal values. However, the `#` modifier appends the decimal point, so anybody can know that this is a floating-point value.






## Credits

- [Python's Format Mini-Language for Tidy Strings](https://realpython.com/python-format-mini-language/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-01-30#using-string-interpolation-and-replacement-fields)
