# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.

# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를
# 색종이의 변과 도화지의 변이 평행하도록 붙인다.
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후
# 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.

# 입력

# 첫째 줄에 색종이의 수가 주어진다.
# 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데
# 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고,
# 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다.
# 색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다.

# 출력

# 첫째 줄에 색종이가 붙은 검은 영역의 둘레의 길이를 출력한다.


def check(_x, _y):
    global floor, answer

    try:
        if floor[_x][_y] == 0:
            answer += 1
    except IndexError:
        answer += 1


N = int(input())

floor = [[0] * 100 for i in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for arr in floor[x:x+10]:
        arr[y:y+10] = [1] * 10

answer = 0
for x in range(len(floor)):
    for y in range(len(floor[x])):
        if floor[x][y] == 1:
            check(x + 1, y)
            check(x - 1, y)
            check(x, y + 1)
            check(x, y - 1)

print(answer)
