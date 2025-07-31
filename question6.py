def find_first_negative(lst):
    """
    This function finds the first negative number in a list using a while loop.
    Returns the first negative number if found, otherwise returns "No negatives".
    """
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"

# Example 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("First negative 1:", result1)

# Example 2
result2 = find_first_negative([2, 10, 7, 0])
print("First negative 2:", result2)
