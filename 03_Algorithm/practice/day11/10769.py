# 10769번 행복한지 슬픈지
'''
행복 = :-)
슬픔 = :-(

출력
- no emoticon => none
- 행복 = 슬픔 -> unsure
- 행복 > 슬픔 -> happy
- 행복 < 슬픔 -> sad
'''
# 개수에 따른 조건문 필요
# ':-)' ':-(' string / 카운팅

strings = input()
happy_emoji = ':-)'
sad_emoji = ':-('

# 행복 이모티콘이 더 많다면
if strings.count(happy_emoji) > strings.count(sad_emoji):
    print('happy')

# 슬픈 이모티콘이 더 많다면
elif strings.count(happy_emoji) < strings.count(sad_emoji):
    print('sad')

# 같다면
elif strings.count(happy_emoji) == strings.count(sad_emoji):

    # 적어도 하나는 있다면
    if strings.count(happy_emoji) >= 1:
        print('unsure')

    # 아예 없다면
    else:
        print('none')