def highest_frequency_element(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    max_freq = max(freq.values())

    for key, value in freq.items():
        if value == max_freq:
            return key


nums = [1, 2, 3, 2, 2, 1, 3, 1, 2, 5, 2]
print(highest_frequency_element(nums))
