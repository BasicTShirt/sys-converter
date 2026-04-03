# Last Big Update: 1.1.0

### - Added Support For Negative Numbers.
### - A New Function «resys» For Converting To Decimal.
### - New Error Handler.
### - New Readme.

---

# Sys Converter

A library for converting numbers to different number systems (from binary to base-36).

## Features

- Convert integers to any number system (2-36).
- Convert fractional numbers with precision up to 10 decimal places.
- Error handling with clear messages.
- Support for floating-point numbers.

## Installation

```bash
pip install sys-converter
```

---

## Usage

- To import, use «from sys_converter import *» or «from sys_converter import sys, resys».
- To use the library functions, use the command «sys(number: int, number_system_base: int)» or «resys(number: str, number_system_base: int)».

### For example

#### This program accepts an integer (int) as input and outputs this number in the base-4 number system.

```python
from sys_converter import sys

temp_num = int(input()) # Input: 26
new_num = sys(temp_num, 4)

print(new_num) # Output: 122
```
## Requirements

- Python 3.6 or higher.
- No external dependencies (uses only standard library).

---

## Limitations

| Limitation                 | Details                                           |
|----------------------------|---------------------------------------------------|
| **Maximum base**           | 36 (uses digits 0–9 and letters A–Z)              |
| **Fractional precision**   | Fixed at 10 decimal places                        |
| **Input type**             | Integer, float or string only (look at «Usage»)   |

## Error Handling

The library includes a comprehensive error handling system that validates inputs and provides clear, informative error messages.

### Error Types
| Error                     | Description                                            |
|---------------------------|--------------------------------------------------------|
| **Base out of range**     | The number system base must be between 2 and 36        |
| **Base is not an integer** | The base parameter cannot be a floating-point number  |
| **Base is missing**       | The base parameter is required                         |
### Error Examples

```python
from sys_converter import *

# Invalid base (greater than 36)
result = sys(42, 37)
print(result)
# Output:
# ERROR! The base of the number system cannot be greater than 36

# Invalid base (less than 2)
result = sys(42, 1)
print(result)
# Output:
# ERROR! The base of the number system cannot be less than 2

# Base as float
result = sys(42, 4.5)
print(result)
# Output:
# ERROR! The base of the number system cannot be float number

# Not a number
result = resys("-4-2", 10)
print(result)
# Output:
# ERROR! The converted number is not a valid integer

# Multiple errors (all displayed)
result = sys(-42, 1.5)
print(result)
# Output:
# ERROR! The base of the number system cannot be less than 2
# ERROR! The base of the number system cannot be float number
```
---

## Changelog

| Version   | Date       | Commit                                                                                                    |
|-----------|------------|-----------------------------------------------------------------------------------------------------------|
| **0.1.0** | 10.03.2026 | Beta: First Beta Version On PyPI                                                                          |
| **0.1.1** | 10.03.2026 | Beta: Fixed Critical Bugs                                                                                 |
| **0.1.2** | 10.03.2026 | Beta: Fixed Critical Bugs And New Error Handling                                                          |
| **1.0.0** | 31.03.2026 | Release: New Readme                                                                                       |
| **1.0.1** | 31.03.2026 | Release: New Readme                                                                                       |
| **1.0.2** | 31.03.2026 | Release: Without Changes                                                                                  |
| **1.1.0** | 02.04.2026 | Release: Added Support For Negative Numbers, A New "resys" Function, A New Error Handler And A New Readme |
| **1.1.1** | 02.04.2026 | Release: Fixed Critical Bugs                                                                              |
| **1.1.2** | 02.04.2026 | Release: Fixed Critical Bugs                                                                              |
| **1.1.3** | 03.04.2026 | Release: Fixed Error Handler Bugs                                                                         |
| **1.1.4** | 03.04.2026 | Release: Added Support Float Numbers For «resys» Function And A New Error Handler                         |

---
###### **Made by the Hi Team.**
