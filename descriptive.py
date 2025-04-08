def mean(numbers):
    """return the mean of number"""
    return sum(numbers)/len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 != 0:
        index_pos = len(sorted_numbers) // 2
        median_value = sorted_numbers[index_pos]
    
    return median_value


