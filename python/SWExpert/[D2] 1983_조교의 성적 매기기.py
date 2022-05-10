T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for tc in range(1, T+1):
    N, K = map(int, input().split())
    students = [[int(x) for x in input().split()] for i in range(N)]

    result = []
    for n in range(N):
        score = students[n][0] * 0.35 + \
            students[n][1] * 0.45 + students[n][2] * 0.2
        result.append(score)

    k_idx = result[K-1]

    # 학생의 점수 순서대로 내림차순 정렬.
    result.sort(reverse=True)

    rate = N // 10

    final_grade = result.index(k_idx) // rate

    print(f'#{tc} {grades[final_grade]}')
