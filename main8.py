# Вывести наиболее часто встречающийся символ

string = 'ababbaababaaa'

slovar = {}
ans = 0
for i in string:
    if i not in slovar:
        slovar[i] = 0
    slovar[i] += 1

for key in slovar:
    if slovar[key] > ans:
        ans = slovar[key]

print(ans)