"""
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
    Kelompok: 10

    Nama Anggota:
    1. Ahmad Afredo Farikh Asfiya - 23091397150
    2. Aditya Revangga Dwi Putra - 23091397167
    3. Yosion Besty Marpaung - 23091397168
"""

#Harga Awal
total_harga = 0

#Menampilkan Menu
print(
    """
    Topping Pizza :
    1. Frankfurter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """)

#Memilih Topping Pizza yang ingin dimakan
topping_pizza = int(input("Pilih Topping Pizza: "))
if topping_pizza == 1:
    topping_pizza = "Frankfurter BBQ"
elif topping_pizza == 2:
    topping_pizza = "Meat Monsta"
elif topping_pizza == 3:
    topping_pizza = "Super Supreme"
elif topping_pizza == 4:
    topping_pizza = "Super Supreme Chicken"
else:
    print("Pilihan ukuran tidak valid.")
    
#Menampilkan Pilihan Crust dan Pilihan Ukuran
print(
    """
    Pilihan Crust :
    1. Pan
    2. StuffedCrust Cheese
    3. StuffedCrust Sausage
    4. Cheesy Bites
    5. Crown Crust

    Pilihan Ukuran :
    1. Personal
    2. Reguler
    3. Large
    """
)

#Memilih Crust dan Memilih Ukuran
crust_pizza = int(input("Pilih Crust/Tepian Pizza dan Ukuran Pizza: "))
if crust_pizza == 1:
    crust_pizza = "Pan"
    total_harga += 0
    size_pizza = int(input("Pilih Ukuran Pizza :"))
    if size_pizza == 1:
      total_harga += 0
    elif size_pizza == 2:
      total_harga += 57_273
    elif size_pizza == 3:
      total_harga += 89_091
elif crust_pizza == 2:
    crust_pizza = "StuffedCrust Cheese"
    total_harga += 11_818
    size_pizza = int(input("Pilih Ukuran Pizza :"))
    if size_pizza == 1:
      total_harga += 0
    elif size_pizza == 2:
      total_harga += 65_455
    elif size_pizza == 3:
      total_harga += 104_545
elif crust_pizza == 3:
    crust_pizza = "StuffedCrust Sausage"
    total_harga += 9_091
    size_pizza = int(input("Pilih Ukuran Pizza :"))
    if size_pizza == 1:
      total_harga += 0
    elif size_pizza == 2:
      total_harga += 64_545
    elif size_pizza == 3:
      total_harga += 102_727
elif crust_pizza == 4:
    crust_pizza = "Cheesy Bites"
    total_harga += 13_636
    size_pizza = int(input("Pilih Ukuran Pizza :"))
    if size_pizza == 1:
      total_harga += 0
    elif size_pizza == 2:
      total_harga += 66_364
    elif size_pizza == 3:
      total_harga += 107_273
elif crust_pizza == 5:
    crust_pizza = "Crown Crust"
    total_harga += 11_818
    size_pizza = int(input("Pilih Ukuran Pizza :"))
    if size_pizza == 1:
      total_harga += 0
    elif size_pizza == 2:
      total_harga += 65_455
    elif size_pizza == 3:
      total_harga += 104_545
    
#Memilih Pake tambahan keju atau tidak
extra_cheese = input("Pakai Tambahan Keju (y/n): ").lower()
while extra_cheese not in ["y", "n"]:
    extra_cheese = input("Pakai Tambahan Keju (y/n): ").lower()
if extra_cheese == "y":
    total_harga += 13_636
    extra_cheese = True
elif extra_cheese == "n":
    extra_cheese = False

#Memunculkan Hasil Pemesanan
print("\nTerima Kasih telah membeli Pizza di Pizza Hut")
print(f"Pesanan Anda Pizza dengan Topping {topping_pizza}")
print(f"Crust/Pinggiran {crust_pizza} dan")
print(f"Pilihan Size {size_pizza}")
print(f"{'dengan' if extra_cheese else 'tanpa'} Tambahan Keju")
print(f"Total Harga: Rp {total_harga}")
