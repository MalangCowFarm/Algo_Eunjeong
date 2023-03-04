# 교수님 풀이 참고
N = int(input())
result = []

for i in range(N+1):
    tmp = [N, i]
    x = N
    idx = 1
    while x >= 0:
        x = tmp[idx-1] - tmp[idx]
        if x >= 0:
            tmp.append(x)
        idx += 1

    if len(tmp) > len(result):
        result = tmp

print(len(result))
print(*result)

