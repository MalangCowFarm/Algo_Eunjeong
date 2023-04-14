import sys
sys.setrecursionlimit(10**5)
### 재귀 호출 가능 횟수 증가시키기

def DFS(start):
    visited[start] = 1      ## 방문 표시
    for i in arr[start]:    ## start번과 연결되어 있는 정점 중에서
        if visited[i] == 0: ## 간 적 없으면 재귀 호출
            DFS(i)


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
for j in range(1, N+1):
    if visited[j] == 0:     ## 1부터 N까지 방문한 적 없는 곳에 대해 함수 호출
        DFS(j)
        cnt += 1            ## 연결 요소 개수 += 1

print(cnt)