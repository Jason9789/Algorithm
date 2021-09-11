
# Binary Search
def binarySearch(A, item, left, right):

    resultLeft = 0
    resultRight = 0
    result = 0
    flag = False

    if left <= right:
        mid = (left + right) // 2
        if item == A[mid]:
            flag = True
            return mid
        elif item < A[mid]:
            return binarySearch(A, item, left, mid-1)
        else:
            return binarySearch(A, item, mid+1, right)
    else:
        if flag == False:
            resultLeft = abs(k - A[left])
            resultRight = abs(A[right] - k)

            result = A[left] if resultLeft <= resultRight else A[right]

        return result

# 입력
n = int(input())
sortedList = [int(x) for x in input().strip().split()]
k = int(input())

print(binarySearch(sortedList, k, 0, n-1))




