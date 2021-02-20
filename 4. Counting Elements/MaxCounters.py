# MaxCounters
# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.


def solution(N, A):
    answer = [0] * N

    current_max = 0
    last_called_max = 0

    for i in A:
        if i == N + 1:
            last_called_max = current_max
        else:
            if answer[i - 1] < last_called_max :
                answer[i - 1] = last_called_max + 1
            else :
                answer[i - 1] += 1

            if answer[i - 1] > current_max :
                current_max = answer[i - 1]

    for i in range(len(answer)) :
        if answer[i] < last_called_max :
            answer[i] = last_called_max

    return answer


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))

# 시간초과
# 해결 방법
# 1) answer 의 max 값을 N + 1이 나왔을 때 계산하는게 아니라 지속적으로 계산한다.
# 2-1) N + 1이 나왔을 경우 다른 변수에 현재 max 값을 저장하고,
# 2-2) 다음에 N + 1이 아니면 max 값과 answer 값을 비교하여 answer 가 작으면 해당 인덱스에 max + 1을 저장한다.
# 시간 복잡도 : O(N * M) ---> O(N + M)
# 이런 아이디어를 어떻게 생각해내는건지...
