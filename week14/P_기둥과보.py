def solution(n, build_frame):
    answer = []

    # answer 내의 모든 값에 대해 확인해서 패스해야 True!
    def check(answer):
        for x, y, num in answer:
            if num:   # 보
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                return False  # 조건 미충족 시 return False로 종료

            else:   # 기둥
                if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                    continue
                return False
        return True


    for x, y, a, b in build_frame:
        # 설치/삭제 후 문제 없는지 확인
        # 문제 있다면 다시 삭제하거나 추가하여 해당 작업 무시
        if b:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    answer.sort()
    return answer


n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))

