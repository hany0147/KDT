# 2941번, 크로아티아 알파벳
'''
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. 
lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
'''
words = input()

if 'c=' in words:
    words = words.replace('c=', '1')
if 'c-' in words:
    words = words.replace('c-', '2')
if 'dz=' in words:
    words = words.replace('dz=', '3')    
if 'd-' in words:
    words = words.replace('d-', '4')
if 'lj' in words:
    words = words.replace('lj', '5')
if 'nj' in words:
    words = words.replace('nj', '6')
if 's=' in words:
    words = words.replace('s=', '7')
if 'z=' in words:
    words = words.replace('z=', '8')

# print(words)
print(len(words))