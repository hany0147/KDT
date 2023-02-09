

ind_1, ind_2, ind_3 = list(map(int, input().split()))

if ind_1 == ind_2 == ind_3: # 눈이 모두 같다면
    print(f'{10000 + ind_1 * 1000}')
elif ind_1 == ind_2 or ind_1 == ind_3 or ind_2 == ind_3: # 눈이 두 개만 같다면
    if ind_1 == ind_2:
        print(f'{1000 + ind_1 * 100}')
    elif ind_1 == ind_3:
        print(f'{1000 + ind_1 * 100}')
    elif ind_2 == ind_3:
        print(f'{1000 + ind_2 * 100}')

else:
    print(f'{max(ind_1, ind_2, ind_3) * 100}')