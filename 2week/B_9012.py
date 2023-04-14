T = int(input())

for tc in range(T):
    ps = input()
    stack = []
    
    for n in ps:
        if n == '(':
            stack.append(n)
        elif n == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(n)
                break
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


# 지난 균형잡힌 세상(4949) 문제와 동일한 방식으로 풀이