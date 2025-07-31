def update_dictionary(dct, key, value):
    """
    This function updates a dictionary with a new key-value pair.
    If the key already exists, it prints the original value before updating.
    """
    if key in dct:
        print("Original value:", dct[key])
    
    dct[key] = value
    return dct

# Example 1
result1 = update_dictionary({}, "name", "Alice")
print("Updated dictionary 1:", result1)

# Example 2
result2 = update_dictionary({"age": 25}, "age", 26)
print("Updated dictionary 2:", result2)
