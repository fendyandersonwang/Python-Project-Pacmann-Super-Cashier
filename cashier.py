from tabulate import tabulate
import pandas as pd

class Transaction:

  def __init__(self):
    """
    Menginisialisasi dictionary cart dan Variable sum
    """
    self.cart = dict()
    self.sum = 0

  def check_order(self):
    """
    Menampilkan detail order yang ada di dalam keranjang
    """
    print("Keranjang:")

    df = pd.DataFrame(self.cart)
    headers = ['Nama Item', 'Harga', 'Kuantitas', 'Total']
    print(tabulate(df.T, headers))
    for key in self.cart:
      self.sum += self.cart[key][2]
    print(f'Total = Rp{self.sum:,}')
    print()

  def add_item(self, item_name, item_price, item_qty):
    """
    Menambahkan item ke dalam keranjang
    """
    item_price_total = item_price * item_qty
    if item_name not in self.cart:
      self.cart[item_name] = [item_qty, item_price, item_price_total]
    else:
      self.cart[item_name][0] += item_qty


  def update_item_name(self, item_name, updated_item_name):
    """
    Mengupdate nama item dalam keranjang
    """
    self.cart[updated_item_name] = self.cart.pop(item_name)
    print(f"Item {item_name} telah diupdate menjadi {updated_item_name}")


  def update_item_price(self, item_name, updated_item_price):
    """
    Mengupdate harga item dalam keranjang
    """
    self.cart[item_name][0] = updated_item_price
    print(f"Harga Item {item_name} telah diupdate menjadi {updated_item_price}")

  def update_item_qty(self, item_name, updated_item_qty):
    """
    Mengupdate kuantitas item dalam keranjang
    """
    self.cart[item_name][1] = updated_item_qty
    print(f"Kuantitas Item {item_name} telah diupdate menjadi {updated_item_qty}")

  def delete_item(self, item_name):
    """
    Menghapus item dalam keranjang
    """
    self.cart.pop(item_name)

  def reset_transaction(self):
    """
    Mereset item dalam keranjang
    """
    self.cart.clear()

  def total_price(self):
    """
    Menampikan detail transaksi berupa item, kuantitas, harga, total,
    dan total yang harus dibayar setelah diskon beserta jumlah
    yang berhasil dihemat
    """
    self.check_order()

    discount = 0
    if self.sum > 500000:
      discount = 0.1
    elif self.sum > 300000:
      discount = 0.08
    elif self.sum > 200000:
      discount = 0.05

    if discount > 0:
      discounted_price = self.sum * discount
      self.sum -= discounted_price
      print(f"Diskon {discount * 100:.0f}%")
      print(f"Anda menghemat Rp -{discounted_price:.2f}")
      print(f"Total yang harus dibayar: {self.sum}")