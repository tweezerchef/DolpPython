def highest_frequency(arr):
    """Return the element with the highest frequency in the array."""
    # Create a dictionary to store the frequencies of each element.
    frequencies = {}
    for element in arr:
        if element not in frequencies:
            frequencies[element] = 0
        frequencies[element] += 1

    # Find the element with the highest frequency.
    highest_frequency = max(frequencies.values())
    highest_frequency_element = None
    for element, frequency in frequencies.items():
        if frequency == highest_frequency:
            highest_frequency_element = element

    return highest_frequency_element


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 1, 2, 3, 2]
    print(highest_frequency(arr))  # 1
