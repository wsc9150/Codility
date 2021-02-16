# OddOccurrencesInArray
# Find value that occurs in odd number of elements.


def solution(A):
    answer = 0

    A.sort()

    while True:
        if len(A) >= 2:
            e1 = A.pop()
            e2 = A.pop()

            if e1 != e2:
                answer = e1
                break
        else:
            answer = A[0]
            break

    return answer


A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))
