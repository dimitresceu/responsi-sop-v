print("1. Manajemen RAM")
print("")

print("Masukkan dalam satuan Mbps! ")
ram = int(input("Kapasitas RAM = "))
sistem_operasi = int(input("Kapasitas RAM yang digunakan sistem operasi = "))
print("------------------")
petabit = int(input("Total petabit = "))
program1 = int(input("Kapasitas RAM yang digunakan program 1 = "))
program2 = int(input("Kapasitas RAM yang digunakan program 2 = "))

konvert_ram = ram*1000 #konversi satuan dari Mbps ke Kbps
konvert_os = sistem_operasi*1000 #konversi satuan dari Mbps ke Kbps
total_program = program1 + program2
ram_terpakai = konvert_os + total_program
perpetabit = konvert_ram / petabit
blok_1 = ram_terpakai / petabit
ram_tidakterpakai = konvert_ram - ram_terpakai
blok_0 = perpetabit - blok_1

print("")
print("========= Hasil =========")
print("")

print("Total RAM = " +str(ram)+ " x 1000")
print("Total RAM = " +str(konvert_ram))
print("------------------")
print("")

print("Petabit = " +str(petabit))
print("------------------")
print("")

print("Kapasitas per petabit = " +str(konvert_ram)+ " : " +str(petabit))
print("Kapasitas per petabit = " +str(perpetabit))
print("------------------")
print("")

print("RAM terpakai = " +str(konvert_os)+ " + " +str(total_program))
print("RAM terpakai = " +str(ram_terpakai))
print("------------------")
print("")

print("RAM tidak terpakai = " +str(konvert_ram)+ " - " +str(ram_terpakai))
print("RAM tidak terpakai = " +str(ram_tidakterpakai))
print("------------------")
print("")

print("Blok 1 = " +str(ram_terpakai)+ " : " +str(petabit))
print("Blok 1 = " +str(blok_1))
print("------------------")
print("")

print("Blok 0 = " +str(perpetabit)+ " - " +str(blok_1))
print("Blok 0 = " +str(blok_0))
