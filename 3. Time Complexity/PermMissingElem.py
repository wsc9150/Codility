# PermMissingElem
# Find the missing element in a given permutation.


def solution(A):
    sum_value = sum(A)

    _sum = 0
    for i in range(1, len(A) + 2):
        _sum += i

    missing = _sum - sum_value

    return missing


A = [2, 3, 1, 5]
print(solution(A))
