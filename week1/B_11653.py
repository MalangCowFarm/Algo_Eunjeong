## sol 1 (while)

# n = int(input())

# while n != 0:
#     i = 2
#     if n == 1:
#         break
#     # for i in range(2, n+1):
#     while i < n+1:
#         if n % i == 0:
#             print(i)
#             n = n // i
#         else:
#             i += 1


## sol 2 (재귀함수)

n = int(input())

def func(num):
    for i in range(2, num+1):
        if num % i == 0 and num//i == 1:
            print(i)
        elif num % i == 0:
            print(i)
            return func(num//i)

func(n)