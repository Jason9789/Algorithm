
# Binary Search
def binarySearch(A, item, left, right):

    resultLeft = 0
    resultRight = 0
    result = 0              # 결과값을 위한 변수
    flag = False            # 이진 탐색을 통해 정확한 값을 찾았을 때를 위한 플래그.

    if left <= right:
        mid = (left + right) // 2

        if item == A[mid]:
            # item을 찾았으므로 flag를 True로 전환하고 값을 반환한다.
            flag = True
            return A[mid]

        # 왼쪽 탐색
        elif item < A[mid]:
            return binarySearch(A, item, left, mid-1)

        # 오른쪽 탐색
        else:
            return binarySearch(A, item, mid+1, right)

    # 이진 탐색에서 찾지 못했을 경우
    else:
        if flag == False:

            # k의 값에서 A[left], A[right]만큼 얼마나 떨어져있는지 값을 구한다.
            resultLeft = abs(k - A[left])
            resultRight = abs(A[right] - k)

            # 구한 값을 비교하여 더 작은 값에 가까운 A[] 출력
            result = A[left] if resultLeft <= resultRight else A[right]

        return result

# 입력
n = int(input())
sortedList = [int(x) for x in input().strip().split()]
k = int(input())

# 출력
print(binarySearch(sortedList, k, 0, n-1))




