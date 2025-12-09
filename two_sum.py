def find_two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i

    return None


result = find_two_sum([3, 1, 5, 7, 5, 9], 10)
print(result)
