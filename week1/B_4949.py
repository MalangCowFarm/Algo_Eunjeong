import sys

# stack =[]
# p = 0
while True:
    stack =[]
    p = 0
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            try:
                stack.remove('(')
            except:
                p += 1
                break
        elif i == ']':
            try:
                stack.remove('[')
            except:
                p += 1
                break  
    if p >= 1:
        print('no')
    elif bool(stack) == True:
        print('no')
    else:
        print('yes')


# 개수에 대해서만 균형 맞춘 상태라 문자열 균형으로 수정하기!!