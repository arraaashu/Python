# Package Sorting Function

This project implements a function to categorize packages based on their volume, dimensions, and mass. The goal is to dispatch packages into the appropriate stack: STANDARD, SPECIAL, or REJECTED, according to the criteria outlined below.

## Problem Description

Packages are sorted into three different categories based on their dimensions and mass:

- *Bulky*: A package is considered bulky if its volume (width × height × length) is greater than or equal to 1,000,000 cm³ or any of its dimensions (width, height, or length) is greater than or equal to 150 cm.
- *Heavy*: A package is considered heavy if its mass is greater than or equal to 20 kg.

### Sorting Rules:
1. *REJECTED*: Packages that are both bulky and heavy.
2. *SPECIAL*: Packages that are either bulky or heavy, but not both.
3. *STANDARD*: Packages that are neither bulky nor heavy.

## Function Implementation

The function sort(width, height, length, mass) is designed to classify packages into one of the three categories.

### Parameters:
- width (int): The width of the package in centimeters.
- height (int): The height of the package in centimeters.
- length (int): The length of the package in centimeters.
- mass (int): The mass of the package in kilograms.

### Returns:
- A string representing the stack where the package should be dispatched: "STANDARD", "SPECIAL", or "REJECTED".

## Code

In the .py file of this repo


## Example Usage

python
# Example 1: Package is bulky but not heavy
print(sort(100, 50, 200, 10))  # Output: "SPECIAL"

# Example 2: Package is heavy but not bulky
print(sort(100, 50, 50, 25))   # Output: "SPECIAL"

# Example 3: Package is neither bulky nor heavy
print(sort(100, 50, 50, 10))   # Output: "STANDARD"

# Example 4: Package is both bulky and heavy
print(sort(200, 200, 200, 30)) # Output: "REJECTED"

### Link to Repl.it (if applicable):


---
