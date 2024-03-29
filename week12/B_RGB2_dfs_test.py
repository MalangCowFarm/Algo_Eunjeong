# dfs로 테스트한 건데 시간초과 뜨지만 예제 5개의 답은 맞음
# 반례 있을지도 모르지만 시간제한 빡세지 않다면 이렇게 접근해도 될지도,,?

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
answer = 1e9

for i in range(3):
    stack = []
    stack.append((0, i, arr[0][i]))
    while stack:
        n, prev, total = stack.pop()

        if total > answer:
            continue

        if n == N - 2:
            for k in range(3):
                if k not in (prev, i):
                    answer = min(answer, total+arr[-1][k])
            continue

        for j in range(3):
            if j == prev:
                continue
            stack.append((n+1, j, total+arr[n+1][j]))

print(answer)
