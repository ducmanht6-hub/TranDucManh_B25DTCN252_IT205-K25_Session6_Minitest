# câu 1
item_price = int(input('Nhập đơn giá sản phẩm của bạn: '))
item_quantity = int(input('Nhập số lượng mua: '))

total_price = item_price * item_quantity
if total_price >= 1000000:
    total_discount = total_price * 0.1
    print(f'Giảm 10% tổng tiền, giá sau phải trả: {total_discount}')

# câu 2
password = 123456
for password_check in range(3, 0, -1):
    input_password = int(input(f'Hãy nhập mật khẩu để đăng nhập (còn {password_check} lần): '))
    if input_password == password:
        print('Đăng nhập thành công!')
        exit()
    else:
        print('Mật khẩu sai, vui lòng nhập lại!')
print('Tài khoản đã bị khóa!')

# cây 3
total_product = 0
total_box = 0
while True:
    input_total_product = int(input('Nhập tổng số lượng sản phẩm: '))
    input_total_box = int(input('Nhập số thùng hàng: '))
    if input_total_product < 0:
        print('Số lượng không hợp lệ, bỏ qua thùng này!')
        continue
    elif input_total_product == 0:
        print('Đã kiểm đếm xong, kết thúc quá trình nhập')
        break
    else:
        total_product += input_total_product
        total_box += input_total_box
        print('Tổng số lượng thùng hàng hợp lệ: ', total_box)
        print('Tổng số lượng sản phẩm thu được: ', total_product)