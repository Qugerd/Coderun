import sys


def main():
    n, m = map(int, input().split())
    weight = [list(map(int, input().split())) for _ in range(n)]
    
    weight_path = [[float('inf')] * m for _ in range(n)]
    weight_path[0][0] = weight[0][0]
    
    for i in range(1, n):
        weight_path[i][0] = weight_path[i-1][0] + weight[i][0]

    for j in range(1, m):
        weight_path[0][j] = weight_path[0][j-1] + weight[0][j]

    for i in range(1, n):
        for j in range(1, m):
            weight_path[i][j] = max(weight_path[i - 1][j], weight_path[i][j - 1]) + weight[i][j]

    i, j = n - 1, m - 1
    way = []
    while i > 0 or j > 0:
        if i == 0:
            way.append('R')
            j -= 1
        elif j == 0:
            way.append('D')
            i -= 1
        elif weight_path[i - 1][j] > weight_path[i][j - 1]:
            way.append('D')
            i -= 1
        else:
            way.append('R')
            j -= 1
    way.reverse()

    print(weight_path[n-1][m-1])
    print(' '.join(way))

if __name__ == '__main__':
    main()