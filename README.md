# PENJELASAN
##
Program manajemen data mahasiswa sederhana menggunakan penerapan linked list untuk menyimpan dan mengelola data mahasiswa. Linked list merupakan struktur data linier yang terdiri dari sejumlah elemen atau node yang saling terhubung satu sama lain melalui pointer. Setiap node pada linked list berisi data dan pointer ke node berikutnya.

Dalam program ini, setiap node pada linked list berisi data akun mobile legends, yaitu Nickname, id, dan  server akun. Linked list digunakan untuk menyimpan data akun mobile legends secara dinamis, sehingga memungkinkan pengguna untuk menambah, menghapus, dan memperbarui data mahasiswa dengan mudah.

# PENGGUNAAN

Implementasi program menggunakan data game untuk merepresentasikan setiap node pada linked list. Selain itu, terdapat kelas LinkedList untuk mengelola linked list secara keseluruhan.

Untuk menambahkan data mahasiswa ke dalam linked list, digunakan metode tambah_data_akun() pada kelas LinkedList. Metode ini akan menambahkan data mahasiswa baru ke akhir linked list.

Untuk menampilkan daftar data mahasiswa, digunakan metode tampilkan_data_akun() pada kelas LinkedList. Metode ini akan menelusuri linked list dan menampilkan data mahasiswa pada setiap node.

Untuk menghapus data mahasiswa dari linked list, digunakan metode hapus_data_akun() pada kelas LinkedList. Metode ini akan mencari node dengan Nickname yang sesuai dan menghapusnya dari linked list.

Untuk memperbarui id dari data game, digunakan metode update_id() pada kelas LinkedList. Metode ini akan mencari node dengan Nickname dan id yang sesuai, dan memperbarui nickname dan id pada node tersebut.

Untuk mencari data akun game berdasarkan Nickname, digunakan metode cari_data_akun() pada kelas LinkedList. Metode ini akan menelusuri linked list dan mencari node dengan Nickname yang sesuai.

Dengan menggunakan linked list, program manajemen data mahasiswa sederhana ini dapat membantu pengguna untuk mengelola data mahasiswa dengan mudah dan efisien.
