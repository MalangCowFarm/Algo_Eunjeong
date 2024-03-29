import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
possible = []

for n in range(N):
    for m in range(M):
        if arr[n][m] == 2:
            possible.append((n, m))

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(green_lst, red_lst):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    gq = deque()
    rq = deque()
    cnt = 0
    tmp = 1

    for g in green_lst:
        gq.append(g)
        visited[g[0]][g[1]] = -1

    for r in red_lst:
        rq.append(r)
        visited[r[0]][r[1]] = -1

    while gq and rq:
        for i in range(len(gq)):
        # 시간에 따라서 gq에서 pop해서 이동시키고 그 다음 rq에 대해 진행
        # 그 다음에 시간 tmp 추가해서
        # while gq:
            gx, gy = gq.popleft()
            # 꽃 핀 곳이면 continue
            if visited[gx][gy] == int(1e9):
                continue

            for d in range(4):
                nx = gx + dx[d]
                ny = gy + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
                    continue
                if not visited[nx][ny]:
                    # 방문한 적 없으면 시간 표시하고 gq에 추가
                    visited[nx][ny] = tmp
                    gq.append((nx, ny))

        for j in range(len(rq)):
        # while rq:
            rx, ry = rq.popleft()
            if visited[rx][ry] == int(1e9):
                continue

            for d in range(4):
                nx = rx + dx[d]
                ny = ry + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = -1
                    rq.append((nx, ny))
                    # 방문 기록 남기고 rq에 추가

                elif visited[nx][ny] == tmp:
                    # 만약 visited의 값이 tmp면 초록색 배양액과 합쳐져 꽃피움
                    cnt += 1
                    visited[nx][ny] = int(1e9)
        tmp += 1
    return cnt


for comb in combinations(possible, G+R):
    for green_lst in combinations(comb, G):
        red_lst = []
        for r in comb:
            if r not in green_lst:
                red_lst.append(r)
        result = max(result, bfs(green_lst, red_lst))

print(result)

