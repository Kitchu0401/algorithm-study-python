# 과자 한 개의 가격, 사려고 하는 과자의 개수와 동수가 현재 가진 돈의 액수가 주어질 때 동수가 부모님께 받아야 하는 돈의 액수를 출력하는 프로그램을 작성하시오.

# 입력

# 첫 번째 줄에는 과자 한 개의 가격 K, 사려고 하 는 과자의 개수 N, 현재 동수가 가진 돈 M이 각각 공백을 사이에 두고 주어진다.
# 단, K, N은 1,000 이하의 양의 정수이고, M은 10만 이하의 양의 정수이다. (1 ≤ K,N ≤ 1,000 , 1 ≤ M ≤ 100,000 이다.)

K, N, M = map(int, input().split())

# K * N 은 구매하고자 하는 총 과자의 가격이 되고, M 은 동수가 가진 돈.
# M - (K * N) 의 값이 0 보다 크면 동수가 가진 돈이 충분한 것이고,
# 0보다 작으면 음수값 만큼 부모님에게서 돈을 받아야 하는 것이다.
# min() 을 활용해 위의 두 경우를 구분한 후, abs() 로 양수로 치환하여 답을 출력한다.
print( abs( min(0, M - (K * N)) ) )