# 평면에 색깔이 서로 다른 직사각형 모양의 색종이 N 장이 하나씩 차례로 놓여진다. 
# 이 때 색종이가 비스듬하게 놓이는 경우는 없다. 즉, 모든 색종이의 변은 서로 평행하거나, 서로 수직이거나 둘 중 하나이다.

# N 장의 색종이가 주어진 위치에 차례로 놓일 경우, 각 색종이가 보이는 부분의 면적을 구하는 프로그램을 작성하시오.

"""
2
0 0 10 10
2 2 6 6

64
36

4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10

62
24
0
120
"""

# 색종이의 장수
paper_count = int(input())

# 문제에서는 평면의 크기를 최대 1001 x 1001이라 했지만,
# 본 코드에서는 색종이의 위치와 크기를 따져 평면의 크기를 동적으로 산출했다.
# 계산하지 않고 그냥 1001 x 1001로 생성해도 무관. 오히려 속도는 더 빠를 것.-_-;
max_x = 0
max_y = 0

# 색종이 빈 배열을 먼저 생성한다.
papers = []

# 색종이 장수만큼 for문을 돌며 다음의 로직을 수행한다.
for i in range(paper_count):
    # append()를 통해 배열에 동적으로 요소를 삽입할 수 있다.
    # 색종이 배열에 색종이에 대한 정보를 입력하고,
    # max()를 통해 평면의 최대 가로, 세로 좌표를 구한다.
    papers.append(list(map(int, input().split())))
    max_x = max(max_x, papers[i][0] + papers[i][2])
    max_y = max(max_y, papers[i][1] + papers[i][3])

# 2차원 배열 생성)
# 최대 가로, 세로 좌표 만큼의 평면을 2차원 배열로 구현한다.
# [0] * max_x 에서 길이가 max_x인 배열이 0으로 초기화되어 생성되며,
# 이를 배열 내에서 max_y 만큼 반복하면서 [max_x][max_y] 크기의 이차원 배열이 생성된다.
floor = [[0] * max_x for i in range(max_y)]

# 각 색종이가 차지하는 면적을 입력하기 위한 1차원 배열을 하나 생성한다.
result = [0] * paper_count

# 이후 색종이 장수만큼 for문을 돌며 로직을 수행하는데,
# 이때 range()에 인자를 3개를 넘겨주어 마지막으로 깔린 색종이부터 역순으로 수행한다.
# 다음과 같은 경우 만약 papers의 길이가 5일 경우 i에는 순서대로 5, 4, 3, 2, 1이 들어온다.
for i in range(len(papers), 0, -1):
    # 인덱스로 바꿔주고
    idx = i - 1
    # 2중 for문을 돌며 평면 2차원 배열에 색종이가 깔린 위치를 표시해준다.
    for x in range(papers[idx][0], papers[idx][0] + papers[idx][2]):
        for y in range(papers[idx][1], papers[idx][1] + papers[idx][3]):
            # 만약 해당 공간이 비어있다면 ( floor[y][x] == 0 )
            # 색종이가 놓였다고 표시해주고 floor[y][x] = 1
            # 해당 인덱스의 색종이의 면적을 가산해준다. result[idx] += 1
            if floor[y][x] == 0:
                floor[y][x] = 1
                result[idx] += 1

# 각 색종이가 평면에서 차지한 면적을 차례대로 출력해준다.
for i in range(len(result)):
    print(result[i])

