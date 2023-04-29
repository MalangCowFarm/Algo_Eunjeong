from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

def move(arr, d):
    if d == 0:      # 상
        for j in range(N):  # 열
            end = 0         # 가장 윗줄 == 끝
            for i in range(1, N):   # 1행 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:  # 0이면 끝으로 옮기기
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:  # 같으면 *2
                        arr[end][j] *= 2
                        end += 1
                    else:
                        end += 1                # 다르면 end += 1 해서 값 옮기기
                        arr[end][j] = tmp
                    # arr[i][j] = 0
                    #### arr[i][j]를 end 이용한 위치에 넣고 이후에 0으로 바꾸면 답 안 나옴,,,,

    if d == 1:      # 하
        for j in range(N):
            end = N-1
            for i in range(N-2, -1, -1):  # 밑(end 윗줄)에서부터 위로
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:
                        arr[end][j] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[end][j] = tmp

    if d == 2:      # 좌
        for i in range(N):  # 행
            end = 0
            for j in range(1, N):  # 1열 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end += 1
                    else:
                        end += 1
                        arr[i][end] = tmp

    if d == 3:      # 우
        for i in range(N):
            end = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[i][end] = tmp
    return arr


def dfs(arr, cnt):
    global result
    if cnt == 5:
        for n in range(N):
            result = max(result, max(arr[n]))
        return

    for d in range(4):
        tmp_arr = move(deepcopy(arr), d)
        dfs(tmp_arr, cnt+1)


dfs(input_arr, 0)
print(result)



'''
제일 처음에 for문으로 4방향 탐색할랬는데 모든 방향에 대한 브루트포스 어떻게 할지 막힘 
그래서 이동 함수에서 방향 4개 모두 나눠서 정의함
먼저 방향에 따른 인접칸 확인해서 합칠 수 있으면 합치고 
합치기 다 끝난 후에 끝으로 밀어넣었는데 틀림,,,,
  - 시간초과 걱정했는데 그냥 틀림 
  - 상하/좌우에 따라 행/열 우선조회 달리 해야겠다 싶어서 순서 바꿨는데도 틀림 
  - 생각해보니 붙어 있는 칸에 대해서만 합치고 떨어져 있는 경우 안 합치는 듯함 
그래서 결국 구글링의 도움을 받아서,,,, end라는 방향별 끝 지점을 나타내는 변수 만들고 
상황에 따라 end 조절해가며 값 이동 
  - 코드 길이 줄어들고, 아마 시간도 줄었을 듯 
  - end 위치에 arr[i][j] 값 저장하고 마지막에 기존 위치를 0으로 바꾸면 반례 돌려봤을 때 틀리고 
  - tmp로 별도 저장해서 0으로 바꾼 뒤, 조건문에서 tmp로 넣어주거나 비교해야 함. 
'''