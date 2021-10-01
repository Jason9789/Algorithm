
# Merge Sort
def mergeSort(list):

    # list의 데이터가 하나일 때
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    # left와 right를 비교하여 작은 값들을 sorted_list에 넣어준다.
    while (i < len(left) and j < len(right) ):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # left에 남은 값들을 모두 넣어준다.
    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1

    # right에 남은 값들을 모두 넣어준다.
    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# main
n = int(input())
list = [int(x) for x in input().strip().split()]

result = 500001
sorted_list = mergeSort(list)

# 두 수의 최소 차를 result에 비교하여 저장해놓는다.
for i in range(len(sorted_list)-1):
    result = min(result, sorted_list[i+1] - sorted_list[i])

print(result)