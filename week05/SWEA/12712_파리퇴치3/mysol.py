import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

cx = [-1, -1, 1, 1] # 좌상 우상 좌하 우하
cy = [-1, 1, -1, 1]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for x in range(N):
        for y in range(N):
            tmp1 = arr[x][y]
            tmp2 = arr[x][y]

            for d in range(4):
                for m in range(1, M):
                    nx = x + dx[d] * m
                    ny = y + dy[d] * m
                    if 0 <= nx < N and 0 <= ny < N:
                        tmp1 += arr[nx][ny]

                    mx = x + cx[d] * m
                    my = y + cy[d] * m
                    if 0 <= mx < N and 0 <= my < N:
                        tmp2 += arr[mx][my]

            if tmp1 > result:
                result = tmp1
            if tmp2 > result:
                result = tmp2

    print(f'#{tc} {result}')




# ###########
# for x in range(N):
#     for y in range(N):
#         stack1 = [(x, y)]
#         stack2 = [(x, y)]
#         tmp1 = arr[x][y]
#         tmp2 = arr[x][y]
#
#         for d in range(4):
#             i = 0
#             while stack1:
#                 i += 1
#                 if i == M:
#                     break
#                 x, y = stack1.pop()
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     stack1.append((nx, ny))
#                     tmp1 += arr[nx][ny]
#         if tmp1 > result:
#             result = tmp1
#
#         for c in range(4):
#             j = 0
#             while stack2:
#                 j += 1
#                 if j == M:
#                     break
#                 x, y = stack2.pop()
#                 mx = x + cx[c]
#                 my = y + cy[c]
#                 if 0 <= mx < N and 0 <= my < N:
#                     stack2.append((mx, my))
#                     tmp2 += arr[mx][my]
#
#         if tmp2 > result:
#             result = tmp2
#
# print(f'#{tc} {result}')