 # Aplikasi Inputan data siswa
        
       
import os
import sys

class Mahasiswa:
        nim=''
        nama=''
        
pilih = 0
dataSiswa = []

def menu():
    os.system('cls')
    print("Menu Aplikasi Data Siswa")
    print("----------------------------------------------")
    print("1. Input Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Update Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Author")
    print("6. Keluar Aplikasi")
    pilih = int(input("Masukkan pilihan anda : "))
    if pilih ==1 :
        pilih1()
        menu()
    elif pilih == 2:
        tampil()
        input("Kembali menu utama")
        menu()
    elif pilih == 3:
        index_update=-1
        tampil()
        id_edit = int(input("Input Nim yang akan di update "))
        for a in range(0, len(dataSiswa)):
            if id_edit == dataSiswa[a].nim
                    index_update = a
                    break
        if(index_update > -1):
            print("INPUT DATA YANG DI UPDATE ")
            siswa = Mahasiswa()
            siswa.nim = (int(input("masukkan nim : ")))
            siswa. nama = (input("masukkan nama siswa :"))
            dataSiswa[index_update] = siswa
            print("berhasi
