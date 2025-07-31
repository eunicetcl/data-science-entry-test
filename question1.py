def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x, y = y, x
    print("Swapped values:", x, y)

result1 = swap("Apple", 10)
if result1 == -1:
    print("Invalid input: both values must be numeric.")

result2 = swap(9, 17)
if result2 == -1:
    print("Invalid input: both values must be numeric.")
