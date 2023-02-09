# 2953번 나는 요리사다
'''
각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다.
점수는 1점부터 5점까지 있다.

각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다.
이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

각 참가자가 얻은 평가 점수가 주어졌을 때,
우승자와 그의 점수를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 
첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 
항상 우승자가 유일한 경우만 입력으로 주어진다.
'''
score_dict = {}
max_score = 0

for i in range(1, 6):
    score = list(map(int, input().split()))
    score_dict[i] = sum(score)
    if max_score < sum(score):
        max_score = sum(score)

for key in score_dict:
    if score_dict[key] == max_score:
        print(key, max_score)


# print(score_dict) - > {1: 18, 2: 17, 3: 18, 4: 19, 5: 17}
# 좀 더 괜찮은 방법 없을까?

## 동료 코드

# score = []

# for i in range(5):
#     s = list(map(int, input().split()))
#     score.append(sum(s))

    
# print(score.index(max(score))+1, max(score))