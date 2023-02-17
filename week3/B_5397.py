#### 시간초과
import sys

T = int(input())
for tc in range(T):
    string = sys.stdin.readline().rstrip()
    stack = []
    tmp = []
    result = ''
    
    for s in string:
        if s not in '-<>':
            stack.append(s)
        else:
            if s == '-' and stack:
                stack.pop()
            elif s == '<' and stack:
                tmp_s = stack.pop()
                tmp.append(tmp_s)
            elif s == '>' and tmp:
                tmp_s = tmp.pop()
                stack.append(tmp_s)
    while stack:
        result += stack.pop()
    print(result[::-1])
