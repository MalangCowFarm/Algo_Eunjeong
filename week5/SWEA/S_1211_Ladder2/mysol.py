import sys
sys.stdin = open('input (13).txt')

for t in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000

    for i in range(100):
        if arr[0][i] == 1:
            x, y = 0, i
            cnt = 0

            while x < 99:
                if 0 <= y-1 and arr[x][y-1] == 1:
                    while 0 <= y and arr[x][y-1] == 1:
                        y -= 1
                        cnt += 1
                elif y+1 < 99 and arr[x][y+1] == 1:
                    while y < 99 and arr[x][y+1] == 1:
                        y += 1
                        cnt += 1
                x += 1

            if cnt <= min_cnt:
                min_cnt = cnt
                result = i
    print(f'#{tc} {result}')