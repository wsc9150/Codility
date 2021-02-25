# CyclicRotation
# Rotate an array to the right by a given number of steps.


def solution(A, K):
    length = len(A)

    if length == 0 :
        return A

    r = K % length

    new_arr = []
    for i in range(len(A)):
        new_arr.append(A[(length - r + i) % length])

    return new_arr


A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))
