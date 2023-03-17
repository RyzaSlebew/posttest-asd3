from prettytable import PrettyTable


class Data_Akun:
    def __init__(self, ID, nickname, server_akun):
        self.id = ID 
        self.nickname = nickname
        self.server_akun = server_akun
        self.next = None


class Data_AkunLinkedList:
    def __init__(self):
        self.head = None

    def tambah_Data_Akun(self, ID, nickname, server_akun):
        new_Data_Akun = Data_Akun(ID, nickname, server_akun)

        if not self.head:
            self.head = new_Data_Akun
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Data_Akun


    def tampilkan_Data_Akun(self):
        if not self.head:
            print("Tidak ada data akun yang terdaftar.")
        else:
            current = self.head
            table = PrettyTable(["ID", "Nickname", "Server_Akun"])
            while current:
                table.add_row([current.nickname, current.ID, current.server_akun])
                current = current.next
            print(table)

    def cari_Data_Akun(self, nickname):
        current = self.head
        while current is not None:
            if current.nickname == nickname:
                return current
            current = current.next
        return None



    def update_Data_Akun(self, id, nickname, server_akun):
        Data_Akun = my_list.cari_Data_akun(id)
        if Data_Akun:
            Data_Akun.id = id
            Data_Akun.nickname = nickname
            Data_Akun.server_akun = server_akun
            print("Data akun anda berhasil diupdate!")
        else:
            print("Data akun dengan Nickname tersebut tidak ditemukan.")

    def hapus_Data_Akun(self, nickname):
        current = self.head
        if current and current.nickname == nickname:
            self.head = current.next
            current = None
            print("Data Akun berhasil dihapus")
            return
        prev = None
        while current and current.nickname != nickname:
            prev = current
            current = current.next
        if current is None:
            print("Data Akun dengan Nickname tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Data Akun berhasil dihapus!")



def tampilan_menu():
    print("""
    |========================================|
    |------------DATA AKUN-------------------|
    |========================================|
    |1. Tambah Data Akun Mobile Legends      |
    |2. Tampilkan Data Akun                  |
    |3. Cari Data Akun Mobile Legends        |
    |4. Update Data Akun Mobile Legends      |
    |5. Hapus Data Akun                      |
    |6. Keluar                               |
    |========================================|""")


tampilan_menu()
my_list = Data_AkunLinkedList()

while True:
    pilih = input("Masukan pilihan anda: ")

    if pilih == "1":
        nickname = input("Masukan Nickaname          : ")
        ID = input("Masukan ID         : ")
        server_akun = input("Masukan Nama Server akun : ")
        my_list.tambah_Data_Akun(nickname, ID, server_akun)
        print("Data Akun Mobile Legends berhasil ditambahkan!")
    
    elif pilih == "2":
        my_list.tampilkan_Data_Akun()

    elif pilih == "3":
        nickname = input("Masukan Nickname yang ingin dicari: ")
        Data_Akun = my_list.cari_Data_Akun(nickname)
        if Data_Akun:
            print(f"Data_Akun dengan Nickname {nickname} ditemukan")
            print(f"Nickname : {Data_Akun.nickname}")
            print(f"ID : {Data_Akun.ID}")
            print(f"server_akun : {Data_Akun.server_akun}")
        else:
            print(f"Mah dengan Nickname {nickname} tidak ditemukan.")

    elif pilih == "4":
        my_list.tampilkan_Data_Akun()
        nickname = input("Masukan Nickname Data_Akun yang ingin diupdate: ")
        Data_Akun = my_list.cari_Data_Akun(nickname)
        if Data_Akun:
            nickname_baru = input("Masukan Nickname baru: ")
            ID_baru = input("Masukan ID baru: ")
            server_akun_baru = input("Masukan server_akun baru: ")
            Data_Akun.nim = nickname_baru
            Data_Akun.nama = ID_baru
            Data_Akun.server_akun = server_akun_baru
            my_list.update_mahasiswa(nickname_baru, ID_baru, server_akun_baru)
        else:
            print(f"Data Akun dengan NICKNAME {nickname} tidak ditemukan.")



    elif pilih == "5":
        my_list.tampilkan_Data_Akun()
        nickname = input("Masukan Nickname data akun yang ingin dihapus: ")
        Data_Akun = my_list.cari_Data_Akun(nickname)
        if Data_Akun:
            my_list.hapus_Data_Akun(nickname)
        else:
            print(f"Data akun dengan Nickname {nickname} tidak ditemukan.")

    elif pilih == "6":
        exit()
