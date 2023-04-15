answer = 0


def check(x, y, queen):
    for i in range(x):
        if y == queen[i] or abs(y - queen[i]) == (x - i):
            return False
    return True


def nqueen(x, n, queen):
    global answer
    if x == n:
        answer += 1
        return

    for y in range(n):
        if check(x, y, queen):
            queen[x] = y
            nqueen(x + 1, n, queen)


def solution(n):
    global answer
    queen = [0] * n
    # visited = [0] * n
    nqueen(0, n, queen)

    return answer

print(solution(4))