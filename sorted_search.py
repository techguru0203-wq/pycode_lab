def count_numbers(sorted_list, less_than):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] < less_than:
            left = mid + 1
        else:
            right = mid - 1

    return left

result = count_numbers([1, 3, 5, 7], 4)
print(result)
