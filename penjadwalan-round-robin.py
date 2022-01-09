print("2. Penjadwalan Algoritma Round Robin")
print("")

import os
program = []

def head():
    os.system("cls")

    jml_proses = int(input("Masukkan Jumlah Proses = "))
    print("")

    for i in range(jml_proses):
        nama_program = input("Nama Program : ")
        lama_proses = int(input("Lama Proses Pengerjaan (detik) = "))
        print("")
        program.append([nama_program, lama_proses])

    quantum = int(input("Quantum Time (detik) = "))
    waktu_selesai = 0
    for i in program:
        waktu_selesai += i[1]
    print("")
    print("------------------")
    print("")
    showRR(waktu_selesai, quantum, program)

def showRR(waktu_selesai, quantum, programlist):
    start = 0
    while start < waktu_selesai:
        for i,data in enumerate(programlist):
            nama_prog = data[0]
            lama_prog = data[1]
            sisa = lama_prog - quantum
            
            if(lama_prog >= quantum):
                print(nama_prog, " : \n", start, " - ", start + quantum )
            else:
                print(nama_prog, " : \n", start, " - ", start + lama_prog )
            
            print("")
            if(lama_prog >= quantum):
                start += quantum
            else:
                start += lama_prog
                
            if( sisa > 0):
                program.append([nama_prog, sisa])
head()