# Дан массив целых чисел nums, отсортированный в неубывающем порядке. 
# Вернуть массив квадратов каждого числа, отсортированный в неубывающем порядке.
# outpusts = [0, 1, 9, 16, 100]


nums = [-4, -1, 0, 3, 10]
result = []
l = 0
r = len(nums) - 1

while l <= r:
    if abs(nums[l]) < abs(nums[r]):
        result.append(nums[r] ** 2)
        r -= 1
    else:
        result.append(nums[l] ** 2)
        l += 1
result.reverse()
print(result)













