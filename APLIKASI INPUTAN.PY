#APLIKASI INPUTAN DATA MAHASISWA

import os
import sys

class mahasiswa:
        nama=""
        nim=""
pilih = 0
dataSiswa = []

def Menu () :
        os.system ('cls')
        print("Menu Aplikasi Data Siswa")
        print("-------------------------------------------")
        print("1.Input Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Author")
        print("6. Keluar Aplikasi")
        pilih = int(input("Masukkan Pilihan Anda :"))
        if pilih == 1 :
                pilih1()
                Menu()
                
            elif pilih == 2:
                tampil()
                input("Kembali Ke Menu Utama")
                Menu()
                
            elif pilih == 3:
                index_update=-1
                tampil()
                id_edit = int(input("Input Nim Yang Akan Di Update"))
                for a in range (O, len(dataSiswa)):
                        index_update = a
                        break
