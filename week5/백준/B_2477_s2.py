# 교수님 코드 참고
import sys
input = sys.stdin.readline

K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]

big_w = 0
big_h = 0
small_w = 0
small_h = 0

for i in range(6):
    d, n = lst[i]
    if i % 2:               # 가로 다음 세로, 세로 다음 가로
        if n > big_w:
            big_w = n
    else:
        if n > big_h:
            big_h = n

for i in range(6):
    if i % 2:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_h:          ## (i+-1) % 6 !!!
            small_w = lst[i][1]
    else:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_w:
            small_h = lst[i][1]

result = (big_h * big_w) - (small_h * small_w)
print(result * K)







######## 런타임 에러
# width = {}
# height = {}
# K = int(input())
# for t in range(1, 7):                   # 딕셔너리[인덱스] = 입력값
#     d, n = map(int, input().split())
#     if d in [1, 2]:
#         width[t] = n        # 가로
#     else:
#         height[t] = n       # 세로
#
# max_w = 0
# max_h = 0
# for idx, item in width.items():     # 최대 높이
#     if item > max_w:
#         max_w = item
#         max_w_idx = idx
#
# for idx, item in height.items():    # 최대 너비
#     if item > max_h:
#         max_h = item
#         max_h_idx = idx
#
#
# # 전후 인덱스에 해당하는 값들의 합이 최대 높이/너비라면
# # 해당 인덱스에 해당하는 값은 전체 사각형에서 빼줄 작은 사각형의 높이/너비
# small_w = 0
# small_h = 0
# for idx in range(2, 6):
#     if height[idx-1] + height[idx+1] == max_h:
#         # if height[idx-1] + height[idx+1] == max_h:  1 < idx < 6 and
#         small_w = item
#
# for idx in range(2, 6):
#     if width[idx-1] + width[idx+1] == max_w:
#         # if width[idx-1] + width[idx+1] == max_w:
#         small_h = item
#
# # 전체 큰 사각형의 넓이 - 작은(빈) 사각형의 넓이
# result = (max_h * max_w) - (small_h * small_w)
# print(result * K)

