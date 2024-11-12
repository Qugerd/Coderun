# Найти максимальное число в последовательности и второе по величине число

def findTwoMax(seq):
    first = seq[0]
    second = seq[1]

    for i in range(3, len(seq)):
        if seq[i] > first:
            first = seq[i]
        elif seq[i-1] > second and seq[i-1] < first:
            second = seq[i-1]

    return first, second


nums = [3, 2, 1, 3, 88, 0, 1, 8, 0, -43]

print(findTwoMax(nums))