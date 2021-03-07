# FrogJmp
# Count minimal number of jumps from position X to Y.


def solution(X, Y, D):
    diff = Y - X

    if diff == 0 :
        return 0

    cnt = diff // D

    if diff % D == 0 :
        return cnt
    else :
        return cnt + 1


X = 10
Y = 85
D = 30
print(solution(X, Y, D))
