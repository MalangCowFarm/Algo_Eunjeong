string = input()
cnt = 0
ca_lst = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# 글자 수가 다른 'dz=' 제외한 나머지 알파벳들을 리스트화

while string:
    if string[0:3] == 'dz=':                        
        # 글자수가 가장 긴(3글자) 'dz='와 비교해서 일치하면
        cnt += 1
        string = string.replace(string[0:3], '', 1) # 알파벳 수 +1 하고 해당 글자를 문자열에서 삭제

    elif string[0:2] in ca_lst:
        cnt += 1
        string = string.replace(string[0:2], '', 1)

    else:
        cnt += 1
        string = string.replace(string[0], '', 1)

print(cnt)

