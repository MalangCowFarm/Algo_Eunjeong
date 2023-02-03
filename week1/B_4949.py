import sys

stack =[]
while True:
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
                print('no')
        elif i == ']':
            try:
                stack.remove('[')
            except:
                print('no')    
    if stack:
        print('no')
    else:
        print('yes')


# except랑 stack이 빈 경우랑 중복으로 출력되는 케이스 있음 -> 수정하기