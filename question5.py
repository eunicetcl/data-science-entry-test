def check_divisibility(num, divisor):
    """
    This function checks if num is divisible by divisor.
    Both inputs must be numeric.
    Returns True if divisible, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Invalid input: both values must be numeric.")
        return -1
    
    return num % divisor == 0

# Example 1
result1 = check_divisibility(10, 2)
print("Is 10 divisible by 2?", result1)

# Example 2
result2 = check_divisibility(7, 3)
print("Is 7 divisible by 3?", result2)
