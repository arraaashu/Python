# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:52:12 2024

@author: arraa
"""

def sort(width, height, length, mass):
    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    heavy = mass >= 20
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(100, 50, 200, 10))  # Expected output: "SPECIAL" (bulky)
print(sort(100, 50, 50, 25))   # Expected output: "SPECIAL" (heavy)
print(sort(100, 50, 50, 10))   # Expected output: "STANDARD" (neither bulky nor heavy)
print(sort(200, 200, 200, 30)) # Expected output: "REJECTED" (both bulky and heavy)