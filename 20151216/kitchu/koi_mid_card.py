# 10번의 라운드 순서대로 A와 B가 제시한 카드의 숫자가 주어졌을 때, 게임의 승자를 판단하는 프로그램을 작성하시오.

# 입력

# 첫 번째 줄에는 A가 제시한 카드의 숫자 10개가 라운드 순서대로 주어지고,
# 두 번째 줄에는 B가 제시한 카 드의 숫자 10개가 라운드 순서대로 주어진다.

"""
6 7 5 1 4 10 2 3 8 9
1 10 2 9 4 8 3 7 5 6
"""

# 두 줄로 주어지는 input을 int형 list로 받는다.
aCard = list(map(int, input().split()))
bCard = list(map(int, input().split()))

# for문을 돌면서 10라운드의 종합점수를 산출한다.
# 각 라운드마다 A가 이겼으면 result에 ++를,
# B가 이겼으면 result에 --를 해준다.
result = 0
for i in range(len(aCard)) :
    a = aCard[i]
    b = bCard[i]
    if a > b :
        result += 1
    if a < b :
        result -= 1

# 삼항연산자)
# result가 0보다 크면 A를, 0보다 작으면 B를, 모두 아닐 경우 D를 출력한다.
print( "A" if result > 0 else "B" if result < 0 else "D" )