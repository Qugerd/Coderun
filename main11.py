# Найти максимальное число в последовательности

def findMax(seq):
    ans = float('-inf')
    for i in range(len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


nums = [1, 2, 1, 3, 2]
x = 2

print(findMax(nums))


def findMax2(seq):
    ans = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


nums = [1, 2, 1, 3, 2]
x = 2

print(findMax2(nums))








