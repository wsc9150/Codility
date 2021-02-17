# TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.


def solution(A):
    answer = 0
    sum_list = []

    _sum = 0

    # 접두사 합
    for i in A:
        _sum += i
        sum_list.append(_sum)

    _sum = sum(A)
    for i in range(1, len(A)):
        left_sum = sum_list[i - 1]
        right_sum = _sum - left_sum

        if i == 1 :
            answer = abs(left_sum - right_sum)

        answer = min(answer, abs(left_sum - right_sum))

    return answer


A = [3, 1, 2, 4, 3]
print(solution(A))
