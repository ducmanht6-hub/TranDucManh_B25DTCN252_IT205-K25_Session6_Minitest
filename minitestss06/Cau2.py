password = 123456
for password_check in range(3, 0, -1):
    input_password = int(input(f'Hãy nhập mật khẩu để đăng nhập (còn {password_check} lần): '))
    if input_password == password:
        print('Đăng nhập thành công!')
        exit()
    else:
        print('Mật khẩu sai, vui lòng nhập lại!')
print('Tài khoản đã bị khóa!')
