# 1983번 조교의 성적 매기기
'''
총 10개의 평점
학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영
총점 = 중간고사(0.35)+기말(0.45)+과제(0.2)

10 개의 평점을 총점이 높은 순서대로 부여하는데,
각각의 평점은 같은 비율로 부여할 수 있다.
예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.

학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
'''
import sys
sys.stdin = open('data/1983.txt')

# N은 항상 10의 배수. 따라서 //를 활용
# K학생과 동일 총점을 가진 학생은 없다

T = int(input())

# 1.점수 나열 구현 및 학생 점수 리스트화

for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    student_dict ={}
    scores_lst = []

    for n in range(1, N + 1):
        scores = list(map(int, input().split()))
        total_score = 0.35 * scores[0] + 0.45 * scores[1] + 0.2 * scores[2]
        student_dict[str(n)] = total_score
        scores_lst.append(total_score)

    scores_lst.sort(reverse = True)
    # print(scores_lst)
    # print(student_dict)


    # 2. 점수 매기기

    nums = N // 10
    eval_dict = {}


    eval_dict['A+'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['A0'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['A-'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['B+'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['B0'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['B-'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['C+'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['C0'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['C-'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)
    eval_dict['D0'] = scores_lst[0: nums]
    for num in range(nums):
        scores_lst.pop(0)

    # print(eval_dict)    
    eval_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-','C+', 'C0', 'C-','D0']

    for evaluation in eval_list:
        if student_dict[str(K)] in eval_dict[evaluation]:
            print(f'#{t} {evaluation}')