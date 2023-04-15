dc_lst = []
N = int(input())
rank_lst = []

for n in range(N):
    w, h = map(int, input().split())
    dc_lst.append((w, h))

for i in dc_lst:                # dc_lst의 모든 값 순회
    rank = 1                    # 등수 기본값 1
    for j in dc_lst:
        if i[0] < j[0] and i[1] < j[1]:  # 또 다른 모든 값 순회하면서
            rank += 1                    # w, h 모두 i가 j보다 작으면 i의 등수 + 1 
    rank_lst.append(rank)                # 모든 j 순회 후 i의 등수를 등수 리스트에 추가

print(*rank_lst)

## 처음에 꼬아서 풀다가 도저히 안 되겠어서 구글링 도움 받음,,,
## 브루트 포스 코드 짜는 거에 대해 익숙해지자,,