# 내장 함수

from itertools import permutations, combinations, product, combinations_with_replacement


print(sum([1, 2, 3]))
print(max([1, 2, 3]))
print(min([1, 2, 3]))
print(eval("(1 + 2) * 3"))      # 수학 수식이 문자열 형식으로 들어왔을 때 해당 수식을 계산

a = [3, 2, 1]
print(sorted(a))                # sorted 함수는 그 순간만 소팅 한다. 원본 자체를 변경하진 않는다.
print(a)

a.sort()                        # reverse 속성으로 오름차순, 내림차순을 결정 할 수 있다.
print(a)


# lambda -> 특정 원소를 기준으로 오름차순 혹은 내림차순을 결정한다.
result = sorted([('a', 27), ('b', 11), ('e', 1), ('c', 23)],
                key=lambda x: x[1], reverse=True)

print(result)


# ==================================
# itertools 라이브러리
# ==================================

# permutations : 순열
# combination : 조합
# product : 중복 허용 순열
# combinations_with_replacement : 중복 허용 조합


data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

# 2개를 뽑는 모든 조합 구하기(중복 허용)
result = list(combinations_with_replacement(data, 2))
print(result)
