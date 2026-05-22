item_price = int(input('Nhập đơn giá sản phẩm của bạn: '))
item_quantity = int(input('Nhập số lượng mua: '))

total_price = item_price * item_quantity
if total_price >= 1000000:
    total_discount = total_price * 0.1
    print(f'Giảm 10% tổng tiền, giá sau phải trả: {total_discount}')