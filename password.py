i = 0
while i < 5:
    password = input('請輸入密碼:')
    if password != '123456':
        print('輸入錯誤!')
    if password == '123456':
        print('成功登入!!')
        break 
    if i == 2:
        print('還剩下兩次機會!')
    if i == 3:
        print('還剩下一次機會!')      
    i = i + 1
if i == 5:
    print('登入失敗!!')


