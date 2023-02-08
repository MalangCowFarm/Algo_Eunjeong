emo = ['[',']','(',')']

while True:
    
    word_list = input()
    if word_list =='.':
        break
    emo_str = ''

    for i in str(word_list):
        if i in emo:
            emo_str += i
    while True:
        if len(emo_str)==0:
            print('yes')
            break
        
        if not('[]' in emo_str or '()' in emo_str):
            print('no')
            break

        print(emo_str)
        emo_str = emo_str.replace('[]','')
        emo_str = emo_str.replace('()','')
        


