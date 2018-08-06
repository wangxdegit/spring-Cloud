height = 1.75
weight = 80.5
bmi = 80.5/1.75/1.75
print(bmi)
if bmi<18.5:
    print('轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('重')
elif bmi<32:
    print('肥')
else:
    print('胖')
