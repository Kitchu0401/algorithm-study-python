# 어떤 공연장에는 가로로 C개, 세로로 R개의 좌 석이 C×R격자형으로 배치되어 있다. 각 좌석의 번호는 해당 격자의 좌표 (x,y)로 표시된다.

# 이 공연장에 입장하기 위하여 많은 사람이 대기줄 에 서있다.
# 기다리고 있는 사람들은 제일 앞에서 부터 1, 2, 3, 4, ... 순으로 대기번호표를 받았다.
# 우리는 대기번호를 가진 사람들에 대하여 (1,1) 위치 좌석부터 시작하여 시계방향으로 돌아가면서 비어있는 좌석에 관객을 순서대로 배정한다.

# 여러분은 공연장의 크기를 나타내는 자연수 C와 R이 주어져 있을 때,
# 대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)를 찾는 프로그램을 작성 해야 한다.

# 입력

# 첫 줄에는 공연장의 격자 크기를 나타내는 정수 C와 R이 하나의 공백을 사이에 두고 차례대로 주어진다. 두 값의 범위는 5 ≤ C,R ≤ 1,000 이다.
# 다음 줄에는 어떤 관객의 대기번호 K가 주어진다. 단 1 ≤ K ≤ 100,000,000 이다

# 출력

# 여러분은 입력에 제시된 대기번호 K인 관객에게 배정될 좌석번호 (x,y) 를 구해서 두 값, x와 y를 하나 의 공백을 사이에 두고 출력해야 한다.
# 만일 모든 좌석이 배정되어 해당 대기번호의 관객에게 좌석을 배정할 수 없는 경우에는 0(숫자 영)을 출력해야 한다.

C, R = map(int, input().split())
K = int(input())

# 현재 좌석의 x, y 좌표를 초기화한다.
cur_x = 1
cur_y = 1

# 좌석 탐색을 위한 함수를 정의한다.
# 이 함수는 (문제의 예를 기준으로) 북 - 동 - 남 - 서 순서로 로직을 수행하는데, 그 로직은 다음과 같다.
#   1) 좌석의 번호(K)와 가로(C) 또는 세로(R) 길이를 비교한 후, 낮은 값에서 1을 뺀 값을 구한다.
#   2) 해당 값을 북의 경우 cur_y에 가산, 동의 경우 cur_x에 가산, 남의 경우 cur_y에 감산, 서의 경우 cur_x에 감산한다.
#   3) 동일한 값을 좌석의 번호(K)에 감산해주는데, K 값이 1보다 작거나 같을 경우 함수를 종료한다.
#   4) 최초 북 - 동 - 남 순서대로 로직을 수행 후 이후 서 - 북 - 동 - 남 순서대로 수행하면서부터 threshhold를 고려한다.
def explore():
    global C, R, K
    global cur_x, cur_y

    # 북으로 이동하며 좌석을 탐색
    move = min(K, R) - 1
    cur_y += move
    K -= move

    if K <= 1:
        return

    # 동으로 이동하며 좌석을 탐색
    move = min(K, C) - 1
    cur_x += move
    K -= move

    if K <= 1:
        return

    # 남쪽으로 이동하며 좌석을 탐색
    move = min(K, R) - 1
    cur_y -= move
    K -= move

    if K <= 1:
        return

    threshold = 1

    # 이미 선점된 좌석을 제외해야 하므로, 여기서부터 threshhold를 고려한다.
    while True:
        # 서쪽으로 이동하며 좌석을 탐색
        move = min(K, C - threshold) - 1
        cur_x -= move
        K -= move

        if K <= 1:
            return

        # 북쪽으로 이동하며 좌석을 탐색
        move = min(K, R - threshold) - 1
        cur_y += move
        K -= move

        if K <= 1:
            return

        # 서 - 북 로직 후 threshhold 증가
        threshold += 1

        # 동쪽으로 이동하며 좌석을 탐색
        move = min(K, C - threshold) - 1
        cur_x += move
        K -= move

        if K <= 1:
            return

        # 남쪽으로 이동하며 좌석을 탐색
        move = min(K, R - threshold) - 1
        cur_y -= move
        K -= move

        if K <= 1:
            return

        # 동 - 남 로직 후 threshhold 증가
        threshold += 1

# 만약 좌석 번호(K)가 배정 가능한 최대 번호(C * R) 보다 클 경우
# 문제에서 제시된대로 0을 출력한다.
if (C * R) < K:
    print(0)
# 좌석 배정이 가능한 경우, explore()를 호출 후
# 최종적으로 산출된 좌석의 x, y 좌표를 출력한다.
else:
    explore()
    print('%d %d' % (cur_x, cur_y))
