# 7568번 덩치
'''
사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 
어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.

<조건>
두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 
우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다.
 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 
'''
# 데이터를 어떻게 저장할 것인가?
## dictionary
### dict로 각 사람의 데이터를 수집하고. 비교한다.

N = int(input()) # 사람 수
people_dict = {} # 명단 별 저장.
for n in range(1, N + 1):
    x, y = list(map(int, input().split())) # 몸무게와 키
    people_dict[n] = (x, y)
# print(people_dict)


# 데이터를 어떻게 비교할 것인가?
## if문 
## x도 크고 y도 크면 카운팅한다.
# 이중 for문으로 비교
fin_dict = {}
for num, people in people_dict.items():
    cnt = 1
    for _, compare_p in people_dict.items():
        if people[0] < compare_p[0]:
            if people[1] < compare_p[1]:
                cnt += 1
    fin_dict[num] = cnt 
print(*fin_dict.values())


# 출력을 어떻게 할 것인가?


## 동료코드
# 덩치
# n = int(input())
# n_list = []
# for i in range(n):
#     x,y = map(int,input().split())
#     n_list.append((x,y))

# for i in n_list:
#     rank = 1
#     for j in n_list:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank +=1
#     print(rank, end=' ')
