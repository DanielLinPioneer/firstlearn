print('BMI換算')
H = input('請輸入身高:')
W = input('請輸入體重:')
H = float(H)
W = float(W)
H1 = H / 100 
H1 = H1 * H1
BMI = W / H1

if BMI < 18.5:
    print('BMI值:', BMI, '體重過輕')
elif 18.5 <= BMI < 24:
    print('BMI值:', BMI, '體重正常')
elif 24 <= BMI < 27:
    print('BMI值:', BMI, '體重過重')
elif 27 <= BMI < 30:
    print('BMI值:', BMI, '輕度肥胖')
elif 30 <= BMI < 35:
    print('BMI值:', BMI, '中度肥胖')
else:
    print('BMI值:', BMI, '重度肥胖')
