def top_k_frequent_standard_lib(sequence, k):
    frequency = {}
    for num in sequence:
        frequency[num] = frequency.get(num, 0) + 1
    return sorted(frequency, key=lambda x: frequency[x])[::-1][:k]
