with open('data/fruits.txt', 'r') as f:
    cnt = 0
    for line in f:
        cnt += 1
        # for문으로 각 줄에 있는 문장을 뽑아
        # 그리고 뽑을 때마다 숫자를 더해
    with open('data/02.txt', 'w') as i:
        i.write(str(cnt))
    # 다시 파일 안에 또다른 '쓰기' 파일을 열고,
    #  거기에 해당 숫자를 입력 .write('str')