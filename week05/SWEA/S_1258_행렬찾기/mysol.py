import sys
sys.stdin = open('input (13).txt')


def search(a, b):
    x, y = a, b
    w_cnt = 1
    while True:         # 가로 길이 탐색
        y += 1
        if arr[x][y] == 0 or y < 0 or y >= n:
            # width.append(w_cnt)
            break
        w_cnt += 1

    x, y = a, b
    h_cnt = 1
    while True:  # 세로 길이 탐색
        x += 1
        if arr[x][y] == 0 or x < 0 or x >= n:
            break
        h_cnt += 1

    for i in range(h_cnt):
        for j in range(w_cnt):
            visited[a + i][b + j] = 1
    size_h_w.append([w_cnt*h_cnt, h_cnt, w_cnt])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    size_h_w = []
    result = []

    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0 and visited[x][y] == 0:
                search(x, y)

    size = sorted(size_h_w, key=lambda x: (x[0], x[1]))
    cnt = len(size)
    for i in size:
        result.append(i[1])
        result.append(i[2])

    print(f'#{tc} {cnt}', *result)

