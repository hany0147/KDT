import sys
sys.stdin = open('data/10039.txt', 'r')


scores = []

for i in range(0, 5):
    score = int(input())
    if score >= 40:
        scores.append(score)
    else:
        score = 40
        scores.append(score)

score_avrg = sum(scores) / len(scores)
print(int(score_avrg))