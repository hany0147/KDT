# #++++
# +#+++
# ++#++
# +++#+
# ++++#


# 단순한 프린트 방법
print('#++++\n+#+++\n++#++\n+++#+\n++++#')


print("=========================")


# replace함수 활용

strings = '+++++'

for n in range(1, 6):
  a = strings.replace('+', '#', n)
  # b = a.replace('#', '+', n-1)
  print(a)