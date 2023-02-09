# 17249번 태보태보 총난타

'''
얼굴의 왼편에 왼손의 잔상이, 오른편에는 오른손이 잔상이 남을 때 혜정이는 주먹을 몇 번 뻗었을까?

주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다.
 얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.
'''

taebo = input()
left = 0
right = 0

for lef in taebo[:taebo.index('(')]:
    if lef == '@':
        left += 1
for rig in taebo[taebo.index(')'):]:
    if rig == '@':
        right += 1

print(left, right)
