# Самый дешевый путь
# В каждой клетке прямоугольной таблицы 
# N×M записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).
# Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

import sys

def main():

    N, M = map(int, input().split())
    weight = [list(map(int, input().split())) for _ in range(N)]


    weight_path = [[float('inf')] * M for _ in range(N)]
    weight_path[0][0] = weight[0][0]


    for i in range(N):
        for j in range(M):
            if i > 0:
                weight_path[i][j] = min(weight_path[i][j], weight_path[i-1][j] + weight[i][j])

            if j > 0:
                weight_path[i][j] = min(weight_path[i][j], weight_path[i][j-1] + weight[i][j])


    print(weight_path[N-1][M-1])

if __name__ == '__main__':
    main()