import random

# Quick Sort
def quickSort(A):

    # sort
    def sort(left, right):
        if right <= left:
            return

        mid = partition(left, right)
        sort(left, mid-1)
        sort(mid, right)

    # 피봇에 따라 배열 A 정렬하기
    def partition(left, right):
        # pivot은 랜점하게 선택하기
        pivot = A[random.randrange(left, right)]

        while left <= right:
            while A[left] < pivot:
                left += 1

            while A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left, right = left + 1, right - 1

        return left

    return sort(0, len(A) - 1)


# 입력
n = int(input())
list = [int(x) for x in input().strip().split()]
d = int(input())

# 퀵소트 실행
quickSort(list)
sorted_list = list

start, end = 0, 0           # sorted_list의 index 조정을 위한 변수
result = 0                  # 선택할 수 있는 수들의 최대 개수를 저장하는 변수
result_list = []            # 선택할 수 있는 수들을 저장해 놓는 배열

# start의 값은 비교하기 위한 index를 나타내게 되는데,
# 이 값이 sorted_list -1의 값과 같아졌을 때, 반복문을 종료한다.
# 이는 수행시간 O(n)을 만들기 위함이다.
while start <= len(sorted_list)-1:

    # end index가 sorted_list의 길이와 같아졌을 때,
    # 이때 result_list에 담겨 있는 값을 저장한다.
    if end == len(sorted_list):
        result = max(result, len(result_list))
        result_list.clear()
        break

    # 각 인덱스에 대해서 d보다 작은지 체크하고 작다면 result_list에 값을 저장한다.
    # 그리고 end index를 1 증가시켜 배열의 다음 값과 비교를 한다.
    if (sorted_list[end]-sorted_list[start]) <= d:
        result_list.append(sorted_list[end])
        end += 1

    # 선택할 수 있는 차이가 d 이상이어서, 선택할 수 없을 때
    # 그 순간 result에 담겨 있는 값들을 저장한다.
    # 그 후 start를 1 증가시켜 다음 index에 대해서 두 수의 차를 구할 준비를 한다.
    else:
        result = max(result, len(result_list))
        start += 1
        end = start
        result_list.clear()

print(result)
