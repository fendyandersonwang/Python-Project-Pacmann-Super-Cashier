from cashier import Transaction

test = Transaction()
test.add_item('Ayam Goreng', 2, 20_000)
test.add_item('Pasta Gigi', 3, 15_000)
test.total_price()
test.delete_item('Pasta Gigi')
test.check_order()
test.reset_transaction()
test.check_order()
test.total_price()