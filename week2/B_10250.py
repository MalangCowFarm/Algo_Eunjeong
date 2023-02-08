T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    floor = N % H           # 1호부터 각 층수(H)만큼 채우고 남은 나머지 값이 N번째 고객의 층수가 됨 
    num = (N // H) + 1      # 층수로 나눈 몫이 호수가 되는데, 0이 아닌 1호부터 시작이므로 +1
    if floor == 0:          # 처음에 N % H == 0인 경우 생각 못함
        floor = H           # 만약 나머지가 0이면(6층까지 있는데 6층 배정인 경우)
        num = N // H        # 층수는 나눈 값, 호수는 몫(1, 2, ...)
    result = floor * 100 + num
    print(result)