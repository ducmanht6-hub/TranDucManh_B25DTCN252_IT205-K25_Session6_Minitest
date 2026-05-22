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