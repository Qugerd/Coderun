# Дан целочисленный массив nums, переместить все нули в его конец, 
# сохраняя относительный порядок ненулевых элементов. 
# Обратите внимание, что вы должны сделать это in-place, не создавая копию массива.

# nums = [2, 0, 0, 9, 3, 0, 1]

# slow, fast = 0, 0

# while fast <= len(nums) - 1:
#     if nums[slow] == 0 and nums[fast] != 0:
#         nums[slow], nums[fast] = nums[fast], nums[slow]
#         slow += 1

#     elif nums[fast] == 0 and fast == 0:
#         fast += 1

#     elif nums[slow] != 0:
#         slow +=1

# while slow <= len(nums) - 1:
#     nums[slow] = 0
#     slow += 1

# print(nums)


nums = [2, 0, 0, 9, 3, 0, 1]

slow, fast = 0, 1

while fast <= len(nums) - 1:
    if nums[fast] == 0:
        fast += 1
    elif slow == 0 and nums[slow] != 0:
        slow += 1
    else:
        nums[slow] = nums[fast]
        slow += 1
        fast += 1

while slow <= len(nums) - 1:
    nums[slow] = 0
    slow += 1

print(nums)
