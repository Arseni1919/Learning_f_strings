# F-Strings

## Aligning and Filling the Output
| Value | Description  |
|-------|---|
| <     | Aligns the interpolated value to the left within the available space. It’s the default alignment for most objects.  |
| >     | Aligns the interpolated value to the right within the available space. It’s the default alignment for numbers.  |
| ^     | Aligns the interpolated value in the center of the available space.  |
| =     | Adds padding after the sign but before the digits in numeric values. It’s the default for numbers when 0 immediately precedes the field width.  |


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




## Credits

- [Python's Format Mini-Language for Tidy Strings](https://realpython.com/python-format-mini-language/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-01-30#using-string-interpolation-and-replacement-fields)
- 