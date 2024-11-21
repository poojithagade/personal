


# and Operator: Returns True only if both conditions are True
print((5 > 3) and (10 > 6))  # True, because both 5 > 3 and 10 > 6 are true
print((5 > 3) and (10 < 6))  # False, because 10 < 6 is false even though 5 > 3 is true

# or Operator: Returns True if at least one of the conditions is True
print((5 < 3) or (10 > 6))   # True, because 10 > 6 is true even though 5 < 3 is false
print((5 < 3) or (10 < 6))   # False, because both 5 < 3 and 10 < 6 are false

# not Operator: Inverts the Boolean value
print(not (5 > 3))           # False, because 5 > 3 is true, and 'not' inverts it to false
print(not (5 < 3))           # True, because 5 < 3 is false, and 'not' inverts it to true

'''
These examples illustrate:
- **`and`** only returns `True` if both conditions are true.
- **`or`** returns `True` if at least one condition is true.
- **`not`** flips the result: if it's `True`, it becomes `False`, and vice versa.'''