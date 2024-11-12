# Дана последовательность чисеол длинной N #
# Найти первое (левое) вхождение положительного числа X в нее
# или вывести -1, если число X не встречалось

def findx(seq, x):
    ans = - 1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


nums = [1, 2, 1, 3, 2]
x = 2

print(findx(nums, x))

