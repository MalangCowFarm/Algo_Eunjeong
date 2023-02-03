import sys

def merge_sort(ali):
    if len(ali) == 1:
        return ali
    q = (len(ali)+1) // 2
    left_a = merge_sort(ali[:q])
    right_a = merge_sort(ali[q:])

    ali2 = []
    i = j = 0
    while i < len(left_a) and j < len(right_a):
        if left_a[i] < right_a[j]:
            ali2.append(left_a[i])
            result.append(left_a[i])
            i += 1
        else:
            ali2.append(right_a[j])
            result.append(right_a[j])
            j += 1
    
    while i < len(left_a):
        ali2.append(left_a[i])
        result.append(left_a[i])
        i += 1
    
    while j < len(right_a):
        ali2.append(right_a[j])
        result.append(right_a[j])
        j += 1
    
    return ali2

A, K = map(int, input().split())
ai = list(map(int, sys.stdin.readline().split()))

result = []
merge_sort(ai)

if len(result) >= K:
    print(result[K-1])
else:
    print(-1)
