import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def sol(n):
    visited[n[1]] = 0       # 시작 노드의 visited는 0으로
    q = []
    heappush(q, n)
    while q:
        cost, now = heappop(q)
        if cost > visited[now]:     # 현재 cost가 visited에 저장된 값보다 크면 아래 과정 할 필요 없음
            continue
        for i in node[now]:
            result = cost + i[0]    # cost + 다음 노드로의 가중치
            if result < visited[i[1]]:  # 저장된 값보다 적으면 최소 가중치일 수 있으므로 바꾸기
                visited[i[1]] = result
                heappush(q, (result, i[1]))



V, E = map(int, input().split())
K = int(input())
node = [[] for _ in range(V+1)]
visited = [int(1e9)] * (V+1)

for e in range(E):
    u, v, w = map(int, input().split())
    node[u].append((w, v))      # u노드에 (가중치 w, 도착 정점v) 저장
    ## 앞 인자를 기준으로 정렬하기 때문에
    # 가중치를 기준으로 하기 위해 가중치 먼저 넣어줘야 시간초과 안 뜸


sol((0, K))
for v in visited[1:]:
    if v == int(1e9):
        print('INF')
    else:
        print(v)

