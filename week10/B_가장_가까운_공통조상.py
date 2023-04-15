import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    parent = [0] * (N+1)

    for n in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a   # b의 부모 a

    n1, n2 = map(int, input().split())

    lst = []
    i, j = n1, n2
    while True:
        if i == 0:
            break
        lst.append(i)   # i의 모든 조상 노드 lst에 추가
        i = parent[i]

    while j:
        if j in lst:
            result = j  # 만약 lst에 해당 값이 있으면 그 j가 i와의 공통 조상
            break       # n2부터 시작하므로 가장 가까운 공통 조상 찾게 됨
        j = parent[j]   # j의 조상노드 탐색하면서

    print(result)