import csv #untuk membaca kodingan ini dan menulis nya ke file csv secara otomatis
from prettytable import PrettyTable #untuk menampilkan data dalam format tabel
from pwinput import pwinput #untuk meminta input password dari user saat kodingan dijalankan

multiuser = {} #dictionary untuk menyimpan data user setelah kodingan ini dijalankan dan di isi inputannya yaitu berupa sign up dan sign in
parts_recink = {} #dictionary untuk menyimpan data part racing yaitu berupa nama_part, harga_part
# multiuser sama part_recink tuh kayak database atau save game gitu

def SignUp(): #fungsi untuk mendaftarkan akun baru dengan meminta inputan username, password, privilage lalu ditaro di variabel multiuser dan di print
    username = input("Masukkan username akun baru: ") #untuk masukkan username baru buat akun baru dengan variabel username yang memiliki fungsi input yang berguna untuk mengisi ketikan user
    password = pwinput("Masukkan password akun baru: ") #untuk masukkan password baru buat akun baru dengan variabel password yang memiliki fungsi pwinput yang berguna untuk mengisi ketikan user
    privilage = input("Masukkan privilage (admin/pembeli): ") #untuk masukkan privilage atau perizinan dengan variabel privilage yang memiliki fungsi input yang berguna untuk mengisi ketikan user 
    multiuser[username] = {'password': password, 'saldo e-money': 0, 'parts_recink': [], 'privilage': privilage} #untuk menjadikan wadah untuk variabel username lalu dijadikan wadah yang memiliki fungsi menaruh variabel password, saldo duit, part_recink, dan privilage nya
    print(f"User akun baru {username} berhasil didaftarkan masseh.") #untuk mencetak variabel username yang telah diinput dan diproses dengan fungsi print

def SignIn(): #fungsi untuk memasukkan/log in akun yang telah dibuat di variabel def signup
    username = input("Masukkan username akun: ") #untuk memasukkan username akun yang telah dibuat
    password = pwinput("Masukkan password akun: ") #untuk memasukkan password akun yang telah dibuat
    if username in multiuser and multiuser[username]['password'] == password: # jika username(beserta data data yang telah dibuat di baris 12) didalam variabel multiuser yang sudah ada username beserta passwordnya kalo inputan passwordnya betul sesuai yang sudah dibuat maka berhasil masuk ke username/ log in
        return username #berhasil masokk
    else: #selain itu
        print("Username atau password salah atau takde (belum dibuat akun nya).") #gagal masuk karena inputan tidak sesuai dengan data yang sudah dimasuki ke variabel multiuser
        return None #ndak ngapa ngapain (aksesoris doang )

def recharge_e_money(username): #fungsi untuk menambah saldo ke variabel username
    print(f"Saldo E-Money saat ini: {multiuser[username]['saldo e-money']}")
    jumlah = int(input("Masukkan jumlah saldo E-Money yang ingin ditambahi: ")) #variabel jumlah memiliki fungsi menginput angka bulat yang diketik oleh user beserta keterangan menggunakan str
    multiuser[username]['saldo e-money'] += jumlah #memanggil variabel multiuser yang didalamnya ada data username dan saldo e-money yang masih 0 lalu ditambah menggunakan += variabel jumlah yang telah di input
    print(f"Saldo E-Money berhasil ditambahkan. Saldo E-Money saat ini: {multiuser[username]['saldo e-money']}") #untuk mencetak hasil dari penambahan saldo username yang berada di data multiuser dengan keterangan str
    
def tambah_part(): #fungsi untuk menambah part racing
    nama_part = input("Masukkan nama part racing: ") #untuk memasukkan nama part racing dengan menggunakan fungsi input ke dalam variabel nama_part
    harga_part = int(input("Masukkan harga part racing: ")) #untuk memasukkan harga part racing dengan menggunakan fungsi input ke dalam variabel harga_part
    parts_recink[nama_part] = harga_part #memanggil variabel parts_recink yang berfungsi menyimpan data nama_part yang telah diinput beserta harga_part
    print(f"Part Racing {nama_part} berhasil ditambahkan.") #mencetak data variabel nama_part yang sudah diinputkan beserta harganya dengan keterangan str

def perbarui_part(): #fungsi untuk perbarui part yang sudah diinput di def tambah_part
    table = PrettyTable(['Nama Part Racing', 'Harga'])
    for part, harga in parts_recink.items():
        table.add_row([part, harga])
    print(table)
    nama_part = input("Masukkan nama part racing yang ingin diperbarui: ") #menginput data baru menggunakan fungsi input ke dalam variabel nama_part
    if nama_part in parts_recink: # jika data nama_part yang berada di dalam variabel parts_recink sebagai penyimpanan data
        harga_baru = int(input("Masukkan harga baru: ")) #memasukkan harga baru dengan fungsi input berupa angka bulat ke dalam variabel harga_baru
        parts_recink[nama_part] = harga_baru #memanggil variabel parts_recink yang berfungsi menyimpan data nama_part yang telah diinput beserta harga_baru
        print(f"Harga part racing {nama_part} berhasil diperbarui.") #mencetak data variabel nama_part yang sudah diinputkan beserta harga barunya (angka telah diubah karena variabel harga_baru)
    else: # selain itu
        print("Part racing tidak ditemukan atau salah ketik masseh.") # kalo salah ketik nama part yang telah diinputkan ke dalam variabel nama_part atau memang belum ada datanya di dalam variabel tersebut, maka akan mencetak pesan berikut xixixi

def hapus_part(): #fungsi untuk hapus part yang sudah diinputkan di def tambah_part
    table = PrettyTable(['Nama Part Racing', 'Harga'])
    for part, harga in parts_recink.items():
        table.add_row([part, harga])
    print(table)
    nama_part = input("Masukkan nama part racing yang ingin dihapus: ") #menginput data yang berada di variabel nama_part dengan fungsi input untuk menghapus data di dalam variabel nama_part
    if nama_part in parts_recink: #jika data nama_part yang berada di dalam variabel parts_recink sebagai penyimpanan data
        del parts_recink[nama_part] #menghapus data yang berada di parts_recink yang didalamnya ada data nama_part dengan fungsi del
        print(f"Part racing {nama_part} berhasil dihapus.") # mencetak data dengan fungsi print dengan menyatakan bahwa data yang berada di variabel nama_part sudah dihapus
    else: #selain itu
        print("Part racing tidak ditemukan atau salah ketik masseh.") #kalo salah ketik nama part racing yang berada di dalam variabel nama_part atau memang tidak ada data di dalamnya

def beli_part(username): #fungsi untuk beli part racing sesuai dengan privilage(admin atau pembeli) tiap akun yang berada di variabel username(datanya disitu)
    table = PrettyTable(['Nama Part Racing', 'Harga'])
    for part, harga in parts_recink.items():
        table.add_row([part, harga])
    print(table)
    nama_part = input("Masukkan nama part racing yang ingin dibeli: ") #menginput data dengan fungsi input untuk memanggil data yang berada di dalam variabel nama_part buat beli part racing
    if nama_part in parts_recink: #jika data nama_part yang berada di dalam variabel parts_recink sebagai penyimpanan data
        if multiuser[username]['saldo e-money'] >= parts_recink[nama_part]: #jika data multiuser yang didalamnya ada data dari variabel username beserta saldonya, jika mencukupi maka berhasil membeli part tersebut yang berada di variabel nama_part yang datanya ditaro di part_recink
            multiuser[username]['saldo e-money'] -= parts_recink[nama_part] #jika data multiuser yang didalamnya ada data dari variabel username beserta saldonya, jika tidak mencukupi maka gagal membeli part tersebut yang berada di variabel nama_part yang datanya ditaro di part_recink
            multiuser[username]['parts_recink'].append(nama_part) #setelah berhasil membeli, habistu menambahkan hasil inputan dari variabel nama_part pake append ke variabel multiuser yang didalamnya ada username dan part_recink dengan fungsi input
            print(f"Part racing {nama_part} berhasil dibeli.") #mencetak dengan fungsi print beserta keterangan dengan memanggil variabel nama_part yang telah diinput diatas tadi
        else: #selain itu
            print("Saldo E-Money tidak cukup masseh.") #mencetak dengan fungsi print beserta keterangan jika saldo e-money tidak cukup maka tidak bisa membeli
    else: #selain itu
        print("Part racing tidak ditemukan atau salah ketik masseh.") #mencetak dengan fungsi print beserta keterangan jika salah ketik atau part racing memang belum ada dimasukkan ke dalam data part_recink lewat variabel nama_part ketika diinput

def melihat_part(): #fungsi untuk melihat part racing dengan modul pretty table
    table = PrettyTable(['Nama Part Racing', 'Harga']) #variabel table adalah sebuah wadah untuk menaruh fungsi prettytable biar rapih
    for part, harga in parts_recink.items(): # lalu membuat variabel baru yaitu part dan harga lalu dimasukkan kedalam data variabel part_recink lalu mengembalikan data tersebut dengan fungsi .items
        table.add_row([part, harga]) #memberikan fungsi add_row(nambah baris) ke variabel tabel yang didalamnya ada data variabel part dan harga
    print(table) #mencetak variabel table dengan fungsi print : )

def melihat_invoice(username): #fungsi untuk melihat invoice yang diambil dari data username setelah pemrosesan
    table = PrettyTable(['Nama Part Racing', 'Harga']) #sama kayak diatas
    for part in multiuser[username]['parts_recink']: #untuk melihat data variabel part yang didalamnya ada multiuser dengan memanggil data username yang disitu telah diisi part racing beserta harganya di data 'part_recink'
        table.add_row([part, parts_recink[part]]) #sama kayak diatas nambah baris ke variabel tabel yang didalamnya ada data variabel part yang datanya di variabel part_recink
    print(table) #mencetak variabel tabel dengan fungsi print
    print("Bonus Pembelian keduanya kalinya klo motormu beat mberrr")

def simpan_data(): #fungsi untuk simpan data
    with open('multiuser.csv', 'w') as f: #untuk membuka file bernama ‘multiuser.csv’ dalam mode tulis (‘w’) dan menjadikannya variabel f. habistu fungsi with memastikan bahwa file akan ditutup secara otomatis setelah blok kode di dalamnya selesai di run.
        writer = csv.writer(f) #variabel writer memiliki fungsi menulis ke CSV ke file yang dibuka.
        writer.writerow(['Username Akun', 'Password Akun', 'Saldo E-Money', 'Parts', 'Privilages']) #variabel writer memiliki fungsi menulis baris pertama ke file csv
        for user, data in multiuser.items(): #membuat variabel baru yaitu user dan data lalu dimasukkan kedalam data variabel multiuser lalu mengembalikan data tersebut dengan fungsi .items
            writer.writerow([user, data['password'], data['saldo e-money'], ','.join(data['parts_recink']), data['privilage']]) #variabel writer memiliki fungsi writerow untuk menulis satu baris data ke file CSV. data tersebut memiliki username, password, saldo e-money. lalu dihadirkan data part_recink dengan fungsi join serta privilage

    with open('parts_recink.csv', 'w') as f: #untuk membuka file bernama "part_recink.csv"  dengan fungsi with open dalam mode tulis "w" dan dijadikan variabel f dengan fungsi as 
        writer = csv.writer(f) #variabel writer memiliki fungsi menulis ke csv ke file yang dibuka
        writer.writerow(['Nama Part Racing', 'Harga Part Racing']) #variabel writer memiliki fungsi menulis baris pertama ke file csv
        for part, harga in parts_recink.items(): #membuat variabel baru yaitu part dan harga lalu dimasukkan kedalam data variabel multiuser lalu mengembalikan data tersebut dengan fungsi .items
            writer.writerow([part, harga]) #menulis baris untuk variabel part dan harga

def memuat_data(): #fungsi untuk memuat data
    global multiuser, parts_recink #fungsi global untuk menjadikan variabel multiuser dan part_recink bisa diakses ke semua fungsi
    try: #fungsi try untuk mencoba kode program yang didalamnya
        with open('multiuser.csv', 'r') as f: #untuk membuka file multiuser.csv dengan mode tulis 'r' dan dijadikan variabel f
            reader = csv.reader(f) #fungsi untuk membaca file csv yang dibuka dari atas dengan fungsi .reader
            next(reader)  # Sekip baris header ato baris pertama
            for row in reader: #untuk menjalankan baris yang didalamnya variabel reader
                username, password, saldo, parts_user, privilage = row #menjadikan row sebagai wadah variabel sebelah kiri <<<<
                multiuser[username] = {'password': password, 'saldo e-money': int(saldo), 'parts_recink': parts_user.split(','), 'privilage': privilage} #fungsi Ini untuk menambahkan data pengguna yang telah diinput ke dictionary multiuser.
        
        with open('parts_recink.csv', 'r') as f: #untuk membuka file parts_recink.csv dengan mode tulis "r"
            reader = csv.reader(f) #fungsi untuk membaca file csv yang dibuka dari atas dengan fungsi .reader
            next(reader)  # Sekip baris header
            for row in reader: #untuk menjalankan baris yang didalamnya variabel reader
                nama_part, harga = row #menjadi row sebagai wadah variabel sebelah kiri <<<<<<<<<
                parts_recink[nama_part] = int(harga) #fungsi menambahkan  data dari variabel sebelah kiri <<<<<<<<<<
                
    except FileNotFoundError: #kecuali file tidak ditemukan 
        pass #lanjutkan kodingan tanpa error (lewat gitu)

memuat_data() #fungsi ini memuat data dari file csv di kodingan atas dengan memanggil variabel memuat_data()
while True: #while adalah sebuah fungsi perulangan tidak ada limitnya klo ndak dikasi fungsi break cmiiw
    print("**********************************************#ASMARAKACAU")
    print("**************Jatim SpeedShop*****************#ANTASARI RACEWAY")
    print("**********************************************#PASUKANGHOIB")
    print("Toko Part Recink Yang Membuat Motor Anda Hedon#PLATKTBERDUKA")
    print("**********************************************#NR")
    print("******************PLAT KT*********************#KIRIANSTD")
    print("\n1. Sign Up\n2. Sign In\n3. Exit Masseh") #mencetak dengan fungsi print keterangan str di sebelah kiri <<<<<<<<<<<
    choice = input("Pilihlah opsi bossque: ") #variabel choice memiliki fungsi inputan dengan keterangan pilihlah opsi
    
    if choice == '1': #jika choice sama dengan 1 inputannya maka memanggil variabel signup()
        SignUp() #ada di def Sign Up
        
    elif choice == '2': #jika choice sama dengan 2 inputannya maka memanggil variabel user yang disitu ada data akun yang sudah dibuat dari fungsi signup
        user = SignIn() #^^^^
        if user is not None: #jika user itu lain dengan data yang ada maka akan menampilkan menu lain dan keterangan baris 22 :)
            while True: # ada diatas penjelasannya
                if multiuser[user]['privilage'] == 'admin': #jika data sesuai yg ditaro di variabel multiuser yang menyimpan data user dan privilage dengan yang diinputkan di fungsi sign in, maka berhasil masokk
                    print("\n1. Tambah Part Racing\n2. Perbarui Part Racing\n3. Hapus Part Racing\n4. Lihat Part Racing\n5. Simpan Data ke File CSV\n6. Logout Akun") #mencetak dengan fungsi print keterangan di sebelah kiri <<<<<<<<
                    user_choice = input("Pilihlah opsi bossque: ") #variabel user_choice memiliki fungsi input untuk memilih opsi
                    
                    if user_choice == '1': #jika user_choice sama dengan 1 maka memanggil fungsi tambah_part
                        tambah_part()
                        
                    elif user_choice == '2': #jika user_choice sama dengan 2 maka memanggil fungsi perbarui_pat()
                        perbarui_part()
                        
                    elif user_choice == '3': #jika user_choice sama dengan 3 maka memanggil fungsi hapus_part()
                        hapus_part()
                        
                    elif user_choice == '4': #jika user_choice sama dengan 4 maka memanggil fungsi melihat_part()
                        melihat_part()

                    elif user_choice == '5':
                        simpan_data()
                        
                    elif user_choice == '6': #jka user_choice sama dengan 5 maka memanggil fungsi break atau berhenti
                        break
                        
                    else: #selain itu
                        print("Opsi tidak valdi bruh.") #cetak ini wkwk
                
                elif multiuser[user]['privilage'] == 'pembeli':
                    print("\n1. Tambah Saldo E-Money (sekalian ngeliat saldo) \n2. Beli Part Racing\n3. Lihat Invoice\n4. Simpan Data ke File CSV\n5. Logout Akun Masseh") #cetak ini
                    user_choice = input("Pilihlah opsi bossque: ") #milih lagi
                    
                    if user_choice == '1': #memanggil fungsi recharge_e_money
                        recharge_e_money(user)
                        
                        
                    elif user_choice == '2': #memanggil fungsi beli_part
                        beli_part(user)
                        
                    elif user_choice == '3': #memanggil fungsi melihat_invoice
                        melihat_invoice(user)
                        
                    elif user_choice == '4': #berhenti dengan fungsi break
                        simpan_data()

                    elif user_choice == '5':
                        break
                        
                    else: #selain itu
                        print("Opsi tidak valdi bruh.") #cetak ini
                else:
                    print("SALAH KETIK MASSEH PRIVILAGENYA. CUMAN BISA ADMIN SAMA PEMBELI DOANG : )")  
                    break
    elif choice == '3': #memanggil fungsi break buat stop
        break
        
    else:
        print("Opsi tidak valdi bruh.")
        # baris 164 sampe 174 itu anu nah untuk menu luar tanpa privilage