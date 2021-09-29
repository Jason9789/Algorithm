# 1)
# n (1이상 500000 이하 정수)개의 정수들에 대하여 두 수 차이의 최솟값을 출력하는 프로그램을 작성하시오.
# O(n2) 시간 알고리즘을 이용

n = int(input())
list = [int(x) for x in input().strip().split()]

list.sort()

print(list)
min = list[len(list)-1]

for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        subtract = list[j] - list[i]
        # print(subtract)
        if subtract < min:
            min = subtract


print(min)
