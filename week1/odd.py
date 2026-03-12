def get_odds(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            result.append(nums[i])

    return result


nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))


