### sol 2
n1, n2 = map(int, input().split())

a, b = n1, n2
while True:
    nn = a % b
    a, b = b, nn
    if nn == 0:
        max_n = a
        break

print(max_n)

rest_a = n1 // max_n
rest_b = n2 // max_n
print(max_n * rest_a * rest_b)

# 질문 게시판을 통해 시간 줄이기 위해 유클리드 호제법 사용하는 것을 알게 됨
# 유클리드 호제법 검색해서 어떤 식으로 구상해야할지 고민해서 적용
# n1, n2를 바로 while문에서 계산할 경우 이후 rest 구할 때 0이 돼서 a, b라는 별도의 변수 생성



# ### sol 1 -> 시간초과

# a, b = map(int, input().split())

# i_li = []
# for i in range(1, max(a, b)+1):
#     if a % i == 0 and b % i == 0:
#         i_li.append(i)
# max_i = max(i_li)
# print(max_i)

# for j in range(1, (a*b)+1):
#     rest_a = a // max_i
#     rest_b = b // max_i
# print(max_i * rest_a * rest_b)

