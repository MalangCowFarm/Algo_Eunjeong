import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = N * M

    W_cnt = 0
    for i in range(0, N-2):
        w_tmp_cnt = arr[i].count('W')
        W_cnt += (M - w_tmp_cnt)

        B_cnt = 0
        for j in range(i+1, N-1):
            b_tmp_cnt = arr[j].count('B')
            B_cnt += (M - b_tmp_cnt)

            R_cnt = 0
            for k in range(j+1, N):
                r_tmp_cnt = arr[k].count('R')
                R_cnt += (M - r_tmp_cnt)
                # print(cnt)

            cnt = W_cnt + B_cnt + R_cnt
            if cnt < result:
                result = cnt

    print(f'#{tc} {result}')

