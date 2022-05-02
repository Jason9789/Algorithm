class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1

        return count

        # 모두 0으로 구성된 비트들과의 해밍 거리 풀이식
        # return bin(n).count('1')
