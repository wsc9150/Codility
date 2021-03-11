# PermCheck
# Check whether array A is a permutation.


def solution(A):
    # 최종 합이 맞는지 판단하는 변수
    total = 0
    for i in range(1, len(A) + 1):
        total += i

    # 순열의 모든 수가 있는지 판단하는 변수
    isFlag = True
    A.sort()

    for idx, value in enumerate(A) :
        if value != idx + 1 :
            isFlag = False
            break

    _sum = sum(A)

    if total == _sum and isFlag:
        return 1
    else:
        return 0


A = [1, 4, 1]
print(solution(A))
