def string_reverse(s):
    """
    This function takes a string and returns it reversed.
    If the input is not a string, it returns -1.
    """
    if not isinstance(s, str):
        print("Invalid input: s must be a string.")
        return -1
    return s[::-1]

# Example 1
result1 = string_reverse("Hello World")
print("Reversed 1:", result1)

# Example 2
result2 = string_reverse("Python")
print("Reversed 2:", result2)
