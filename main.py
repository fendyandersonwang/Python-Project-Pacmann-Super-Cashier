from cashier import Transaction

transaction123 = Transaction()
while True:
    print('1. Menambah Item \n2. Mengubah Item \n3. Mengubah Harga Item\
          \n4. Mengubah Kuantitas Item \n5. Hapus Item \n6. Kosongkan Keranjang \n7. Cek Order\
          \n8. Check Out \n0. Keluar')
    choice = int(input('Pilih opsi: '))

    if choice == 0:
        break
    elif choice == 1:
        while True:
            item = input('Masukkan nama item (x untuk exit): ')
            if item == 'x' or item == 'X':
                break
            price = int(input('Masukkan harga: '))
            qty = int(input('Masukkan kuantitas: '))
            transaction123.add_item(item, price, qty)
    elif choice == 2:
        item = input('Masukkan nama item yang ingin diubah: ')
        new_item_name = input('Masukkan nama item baru: ')
        transaction123.update_item_name(item, new_item_name)
    elif choice == 3:
        item = input('Masukkan nama item yang harganya ingin diubah: ')
        new_price = int(input('Masukkan harga baru: '))
        transaction123.update_item_price(item, new_price)
    elif choice == 4:
        item = input('Masukkan nama item yang kuantitasnya ingin diubah: ')
        new_qty = int(input('Masukkan kuantitas baru: '))
        transaction123.update_item_qty(item, new_qty)
    elif choice == 5:
        item = input('Masukkan nama item yang harganya ingin dihapus: ')
        transaction123.delete_item(item)
    elif choice == 6:
        transaction123.reset_transaction()
    elif choice == 7:
        transaction123.check_order()
    elif choice == 8:
        transaction123.total_price()
    else:
        print('Invalid input')