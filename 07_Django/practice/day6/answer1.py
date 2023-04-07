"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)

>> todo = Todo()
>> todo.content = '실습 제출'   
>> todo.priority = 5
>> todo.completed = False
>> todo.deadline = '2023-03-28'  
>> todo.save()
"""

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)

>> todo = Todo(content = '데일리 설문(오후) 제출', deadline = '2023-03-28')
>> todo.save()
"""

"""
3. 임의의 할 일 5개 생성
>>  Todo.objects.create(content = '알고리즘 문제 풀기', priority = 1, deadline = '2023-03-29')
>>  Todo.objects.create(content = 'JS 강의 듣기', priority = 2, deadline = '2023-04-01')
>>  Todo.objects.create(content = '세례받기', priority = 1, deadline = '2023-04-09')
>>  Todo.objects.create(content = '고향가기', priority = 1, deadline = '2023-03-25', completed = True)
>>  Todo.objects.create(content = '영화보기', priority = 3, deadline = '2023-04-02')
"""

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회

>> Todo.objects.order_by('pk')
"""

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회

>> Todo.objects.order_by('-priority')
"""

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)

>> todo_1 = Todo.objects.get(pk=1) 
>> print(todo_1.pk, todo_1.priority, todo_1.deadline, todo_1.created_at)
"""