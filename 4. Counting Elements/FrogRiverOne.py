# FrogRiverOne
# Find the earliest time when a frog can jump to the other side of a river.


def solution(X, A):
    answer = -1

    num_list = set()
    for i in range(len(A)):
        num_list.add(A[i])

        if len(num_list) == X:
            answer = i
            break

    return answer


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))

# 시간초과 이유
# num_list 의 합을 구하는 sum 함수를 for 문 내부에서 사용 -> O(N**2)
# 길이를 구하는 len 함수를 사용해서 시간복잡도가 O(N)으로 감소

# len() : 시간복잡도 O(1)
# sum() : 시간복잡도 O(N)
