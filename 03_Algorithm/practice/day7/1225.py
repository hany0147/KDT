# 1225번 이상한 곱셈
'''
A에서 한 자리를 뽑고 * B에서 임의로 한 자리를 뽑아 곱한다.

의 가능한 모든 조합 (A가 n자리, B가 m자리 수라면 총 가능한 조합은 n*m개)을 더한 수로 정의하려고 한다.

예를 들어 121*34는

1*3 + 1*4 + 2*3 + 2*4 + 1*3 + 1*4 = 28

이 된다. 이러한 형택이의 곱셈 결과를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 A와 B가 주어진다. 주어지는 두 수는 모두 10,000자리를 넘지 않는 음이 아닌 정수이다.
수가 0인 경우에는 0만 주어지며, 그 외의 경우 수는 0으로 시작하지 않는다.
'''
# 시간초과 뜸
# A, B = input().split()
# fin_result = 0
# for a in A:
#     num_a = int(a)
#     for b in B:
#         num_b = int(b)
#         result = num_a * num_b
#         fin_result += result
        
# print(fin_result)

# 재시도(이것도 시간초과)
# A, B = input().split()
# A = list(A)
# B = list(B)
# # print(A, B) -> ['1', '2', '3'] ['4', '5']
# fin_sum_num = 0

# for a in A:
#     num_a = int(a)
#     num = [num_a * int(b) for b in B]
#     # print(num) -> [4, 5] [8, 10] [12, 15]
#     sum_num = sum(num)
#     # print(sum_num) -> 9, 18, 27
#     fin_sum_num += sum_num

# print(fin_sum_num)

# 재재시도
A, B = input().split()
A = list(A)
B = list(B)
B = sum(list(map(int, B)))
fin_sum_num = 0
for a in A:
    a = int(a)
    sum_n = a * B
    fin_sum_num += sum_n

print(fin_sum_num)


## 동료 코드
# A, B = input().split()
# A = list(map(int,A))
# B = list(map(int,B))
# print(sum(A)*sum(B))