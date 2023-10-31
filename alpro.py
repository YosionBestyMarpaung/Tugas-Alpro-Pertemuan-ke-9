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
    1. Frankfurter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """
)

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

#Menampilkan Pilihan Crust
print(
    """
    1. Pan
    2. StuffedCrust Cheese
    3. StuffedCrust Sausage
    4. Cheesy Bites
    5. Crown Crust
    """
)

#Memilih Tipe Crust Pizza
crust_pizza = int(input("Pilih Crust/Tepian Pizza: "))
if crust_pizza == 1:
    crust_pizza = "Pan"
    total_harga = 43_637
elif crust_pizza == 2:
    crust_pizza = "StuffedCrust Cheese"
    total_harga = 55_455
elif crust_pizza == 3:
    crust_pizza = "StuffedCrust Sausage"
    total_harga = 52_728
elif crust_pizza == 4:
    crust_pizza = "Cheesy Bites"
    total_harga = 57_273
elif crust_pizza == 5:
    crust_pizza = "Crown Crust"
    total_harga = 55_455

