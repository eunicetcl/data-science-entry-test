def swap(x, y):
    """
    Task:
    - Swap the values of x and y using only x and y as variables.
    - Both x and y must be numeric (int or float).
    - Return -1 if either x or y is not numeric.
    - Print the swapped values if both are valid.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    x, y = y, x
    print("Swapped values:", x, y)

# Test Case 1: Invalid input
result1 = swap("Apple", 10)
if result1 == -1:
    print("Invalid input: please ensure both values are numeric.")

# Test Case 2: Valid input
result2 = swap(9, 17)
if result2 == -1:
    print("Invalid input: please ensure both values are numeric.")
