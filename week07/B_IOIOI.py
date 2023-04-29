import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input()

result = 0
i = 0
cnt = 0

while i < M:
    if string[i:i+3] == 'IOI':
        i += 2      # 두 칸 뒤(두번째 I부터 탐색)
        cnt += 1    # 'IOI' 개수
        if cnt == N:
            result += 1
            cnt -= 1        # 두 칸 뒤부터 다시 cnt == N인지 확인해야하니까
    else:
        i += 1            # 아닌 경우 한 칸 뒤부터 조사. cnt 초기화
        cnt = 0

print(result)
