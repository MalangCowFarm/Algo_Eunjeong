import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

# 격자 크기 N, 상어 수 M, 이동 수 k
N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
# 상어별 방향 우선순위
directions = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
# 상하좌우 우선순위
smells = [[[0, 0] for _ in range(N)] for _ in range(N)]
# 냄새 시간, 상어 번호
time = 0
sharks = [[0, 0, 0, 0] for _ in range(M+1)]
# 상어 번호별 x좌표, y좌표, 방향, arr에 있는지 저장

### 처음 상어 위치
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            s = arr[i][j]   # 상어 번호
            sharks[s] = [i, j, order[s-1], 1]

def add_smell():  # 상어 위치에 냄새 뿌리기
    for s in range(1, len(sharks)):
        if sharks[s][3]:
            x = sharks[s][0]
            y = sharks[s][1]
            smells[x][y] = [k, s]

def move():
    for s in range(1, len(sharks)):
        if sharks[s][3]:  # arr에 있는 상어 움직이기
            flag = False
            x, y = sharks[s][0], sharks[s][1]
            direc = sharks[s][2]

            for d in directions[s-1][direc-1]:  # 상어 번호별 현재 방향에 대한 방향 우선순위 돌기
                nx = x + dx[d-1]
                ny = y + dy[d-1]

                if 0 <= nx < N and 0 <= ny < N:
                    if not smells[nx][ny][0]:  # 냄새 없으면 그 자리 갈거니까 flag 바꾸고 for문 종료
                        flag = True
                        break

            if not flag:    # 4방향 모두 빈 곳 없으면
                for d in directions[s - 1][direc - 1]:
                    nx = x + dx[d - 1]
                    ny = y + dy[d - 1]

                    if 0 <= nx < N and 0 <= ny < N:
                        if smells[nx][ny][1] == s:  # 자기 냄새 찾아가기
                            break

            if not arr[nx][ny]:  # (nx, ny)에 상어 없으면 그 자리에 저장
                arr[nx][ny] = s
            else:                       # 상어 위치 중복되면 번호 작은 상어 남기기
                if arr[nx][ny] > s:
                    sharks[arr[nx][ny]][3] = 0  # 사라지는 상어의 정보에 arr에 이제 없다는 표시(0) 남기기
                    arr[nx][ny] = s
                else:
                    sharks[s][3] = 0
            arr[x][y] = 0
            sharks[s][0] = nx   # 상어 이동했으니 정보 바꿔줘야함,,,
            sharks[s][1] = ny
            sharks[s][2] = d

def minus_smell():   # 냄새 1씩 감소시키고 0이면 없애기
    for i in range(N):
        for j in range(N):
            if smells[i][j][0]:
                smells[i][j][0] -= 1
                if not smells[i][j][0]:
                    smells[i][j] = [0, 0]

while True:
    time += 1
    if time > 1000:
        break

    add_smell()
    move()
    minus_smell()

    s_cnt = 0
    for i in range(1, M+1):   # 상어 얼마나 남았는지 확인
        if sharks[i][3]:
            s_cnt += 1
    if s_cnt <= 1:
        break

if time > 1000:
    print(-1)
else:
    print(time)



'''
제일 처음에 sharks 정보 저장이 아닌 arr에서 바로 바꿨더니 한 번 이동한 상어가 또 이동하게 됨
그리고 이동이랑 냄새 뿌리기를 한 함수 내에서 정의하고, 남은 냄새의 시간으로 이번 회차에 이동한 상어인지 체크했더니 
테케2에서 자기 냄새가 있는 곳 찾아서 이동하기 전에 
다른 상어가 움직인 곳으로 가서 기존 상어를 쫓아내게 되어서 우선순위가 잘못됨 
그래서 결국 아이디어 도움 받아서 냄새 뿌리기, 이동, 냄새 잔여 시간 감소 세 개로 함수 나눔 
'''
