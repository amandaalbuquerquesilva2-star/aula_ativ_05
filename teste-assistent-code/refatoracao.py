def calculate_statistics(numbers):
    """
    Calculate and return the total, average, maximum, and minimum of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        tuple: (total, average, maximum, minimum)

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list must not be empty.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


# Example usage
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calculate_statistics(data)

print("total:", total)
print("media:", media)
print("maior:", maior)
print("menor:", menor)
