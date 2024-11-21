'''
Here’s a concise one-line definition for each type of conditional statement in Python:

1. **If Statement**: Executes a block of code if a specified condition is `True`.

2. **If-Else Statement**: Executes one block of code if a condition is `True`, and another block if it is `False`.

3. **If-Elif-Else Statement**: Evaluates multiple conditions in sequence and executes the block for the first condition that is `True`.

4. **Nested If Statement**: Contains an `if` statement within another `if` statement, allowing for additional condition checks based on the outer condition's result.
'''

'''weight = int(input("please enter your weight:  "))
measure_type = (input("kg or lb:  "))
kg=0
lb=0
if measure_type == "kg":
    weight_in_lb = float(weight * 2.20462)
    print(round(weight_in_lb))
elif measure_type == "lb":
    weight_in_kg = float(weight / 2.20462)
    print(round(weight_in_kg))
else:
    print("invalid input")
'''


'''Here's a small example of a nested `if` statement in Python. This example checks if a number is positive, negative, or zero, and further checks if it's even or odd if it's positive.

### Example: Nested If Statement

```python
number = 4

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is even.")  # This will print since 4 is even
    else:
        print("It is odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

### Explanation:
1. The outer `if` checks if the number is greater than zero.
   - If `True`, it prints that the number is positive.
   - It then checks if the number is even (using `number % 2 == 0`).
     - If `True`, it prints that the number is even.
     - If `False`, it prints that the number is odd.
2. The `elif` checks if the number is less than zero and prints that it is negative if true.
3. The `else` handles the case where the number is zero. 

This demonstrates how you can use nested `if` statements to check multiple related conditions.'''





