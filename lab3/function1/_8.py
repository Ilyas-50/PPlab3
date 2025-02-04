def spy_game(nums):
    sample = [0, 0, 7]
    count = 0  
    for num in nums:
        if num == sample[count]:
            count += 1
            if count == len(sample):
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  