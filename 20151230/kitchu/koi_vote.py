def count_vote(first_idx, second_idx):
    global result

    first_idx = 0 if first_idx == -1 else first_idx

    for idx in range(3, -1, -1):
        if result[idx][first_idx] > result[idx][second_idx]:
            return first_idx
        if result[idx][first_idx] < result[idx][second_idx]:
            return second_idx

    return -1


N = int(input())

result = [[0] * 3 for i in range(4)]

for _ in range(N):
    scores = list(map(int, input().split()))

    for j in range(len(scores)):
        result[scores[j] - 1][j] += 1
        result[3][j] += scores[j]

max_score = max(result[3])
if result[3].count(max_score) == 1:
    print("%d %d" % (result[3].index(max_score) + 1, max_score))
else:
    print("%d %d" % (count_vote(count_vote(0, 1), 2) + 1, max_score))

"""
6
3 1 2
2 3 1
3 1 2
1 2 3
3 1 2
1 2 3

1 13

10
1 2 3
1 2 3
1 2 3
1 2 3
1 2 3
1 3 2
1 3 2
1 3 2
1 3 2
1 3 2

0 25

50
2 3 1
3 2 1
1 2 3
1 2 3
2 3 1
2 1 3
3 2 1
3 2 1
1 3 2
2 1 3
1 2 3
1 2 3
3 1 2
3 1 2
1 3 2
3 1 2
2 3 1
3 1 2
2 3 1
3 1 2
1 3 2
3 1 2
1 3 2
3 1 2
3 1 2
2 1 3
1 3 2
3 1 2
2 1 3
2 1 3
1 2 3
2 3 1
2 3 1
3 2 1
2 3 1
2 3 1
1 2 3
2 3 1
1 2 3
1 3 2
3 2 1
2 1 3
3 1 2
1 2 3
1 2 3
1 3 2
1 2 3
3 2 1
3 1 2
1 3 2

3 101
"""