import sys
input = sys.stdin.readline

w, h = map(int, input().split())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
result = 0

for i in range(N):
    if lst[i][0] == x:                  # 같은 방향일 때
        result += abs(lst[i][1] - y)
    elif [lst[i][0], x] in [[1, 2], [2, 1]]:    # (남-북)일 때
        d1 = y + lst[i][1]
        d2 = abs(w-y) + abs(w-lst[i][1])
        result += min(d1, d2)
        result += h
    elif [lst[i][0], x] in [[3, 4], [4, 3]]:    #(동-서)일 때
        d1 = y + lst[i][1]
        d2 = abs(h-y) + abs(h-lst[i][1])
        result += min(d1, d2)
        result += w

    else:           # (북-서)와 같이 코너를 중심으로 꺾여있을 때
        if x == 1:
            result += lst[i][1]
            if lst[i][0] == 3:
                result += y
            elif lst[i][0] == 4:
                result += (w-y)
        elif x == 2:
            result += (h - lst[i][1])
            if lst[i][0] == 3:
                result += y
            elif lst[i][0] == 4:
                result += (w-y)
        elif x == 3:
            result += lst[i][1]
            if lst[i][0] == 1:
                result += y
            elif lst[i][0] == 2:
                result += (h-y)
        elif x == 4:
            result += (w - lst[i][1])
            if lst[i][0] == 1:
                result += y
            elif lst[i][0] == 2:
                result += (h-y)

print(result)
