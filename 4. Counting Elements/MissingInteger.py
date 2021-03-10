# MissingInteger
# Find the smallest positive integer that does not occur in a given sequence.


def solution(A):
    A = list(set(A))
    A.sort()

    count = 1
    for i in A:
        if i > 0:
            if i != count:
                break

            count += 1

    return count


A = [1, 3, 6, 4, 1, 2]
print(solution(A))
