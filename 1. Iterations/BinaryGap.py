# BinaryGap
# Find longest sequence of zeros in binary representation of an integer.


def solution(N):
    binary_num = bin(N)[2:]

    count = 0
    gap = [0]

    for i in binary_num:
        if i == '0':
            count += 1
        else:
            gap.append(count)
            count = 0

    return max(gap)


N = 1041
print(solution(N))
