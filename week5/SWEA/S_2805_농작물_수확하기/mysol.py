import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0

    x, y = N//2, N//2               # 중앙 위치
    j = N//2                        # 중앙을 기준으로 양 옆으로 j칸씩 더 가면서 결과에 더해주기
    for l in range(y-j, y+j+1):     # 정중앙의 가로에 대해 result에 더해줌
        result += arr[x][l]

    for i in range(1, N//2+1):      # 정중앙의 x를 기준으로 위아래로 한칸씩 이동(nx1, nx2)
        nx1 = x - i
        nx2 = x + i
        j -= 1                      # 위아래로 이동할수록 양 옆 한 칸씩 줄어듦
        for k in range(y-j, y+j+1):
            result += arr[nx1][k]
            result += arr[nx2][k]

    print(f'#{tc} {result}')

