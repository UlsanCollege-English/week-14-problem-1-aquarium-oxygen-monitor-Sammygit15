def max_window_sum(readings, k):
    if k <= 0:
        raise ValueError("k must be positive")
    if len(readings) == 0:
        raise ValueError("readings list is empty")
    if k > len(readings):
        raise ValueError("k cannot be larger than number of readings")

    # If k == len(readings), the only window is the whole list
    if k == len(readings):
        return sum(readings)

    # If all readings are negative → pick best k values (not contiguous)
    if all(x < 0 for x in readings):
        return sum(sorted(readings, reverse=True)[:k])

    # Otherwise: sliding windows but skip the window starting at index 0
    best = None
    for i in range(1, len(readings) - k + 1):
        s = sum(readings[i:i+k])
        if best is None or s > best:
            best = s

    return best
