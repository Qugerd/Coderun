# Дана последовательность чисел длинной N
# Нйати последнее (правое) вхождение числа X в нее или вывести -1,
# если число X  не встречалось.

def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

nums = [1, 2, 1, 3, 2]
x = 2

print(findx(nums, x))


