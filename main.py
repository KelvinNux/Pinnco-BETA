import subprocess
import time
import sys
import os

def clear_screen():
    # Panggil perintah sistem untuk membersihkan layar terminal
    subprocess.run('clear' if os.name == 'posix' else 'cls', shell=True)

def end_apps():
    clear_screen()


def loading_animation():
    chars = "/—\\|"
    for _ in range(7):  # Ubah angka ini sesuai dengan jumlah iterasi animasi yang diinginkan
        for char in chars:
            sys.stdout.write('\r' + 'memeriksa password ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\n')

def check_password():
    password = "haipin"  # Ganti dengan password yang Anda inginkan
    attempt = input("Masukkan password: ")
    loading_animation()
    return attempt == password

def update_packages():
    try:
        clear_screen()
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        print("Pembaruan paket berhasil diselesaikan.")
    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat memperbarui paket:", e)

def download_wine():
    try:
        clear_screen()
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        print("Pembaruan paket berhasil diselesaikan.")
    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat memperbarui paket:", e)

    try:
        clear_screen()
        subprocess.run(['sudo', 'dpkg', '--add-architecture', 'i386' ], check=True)
        print("Pembaruan paket berhasil diselesaikan.")
    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat memperbarui paket:", e)

    try:
        clear_screen()
        subprocess.run(['sudo', 'mkdir',  '-pm755', '/etc/apt/keyrings' ], check=True)
        print("download berhasil 1/4")
    except subprocess.CalledProcessError as e:
        if e.output:
            print(e.output.decode())  # Menampilkan keluaran dari perintah yang dijalankan
            print("Terjadi kesalahan saat membuat /etc/apt/keyrings ")
    try: 
        subprocess.run(['sudo', 'wget', '-O', '/etc/apt/keyrings/winehq-archive.key' ,'https://dl.winehq.org/wine-builds/winehq.key' ], check=True)
        print("download berhasil 2/4")
    except subprocess.CalledProcessError as e:
        if e.output:
            print(e.output.decode())  # Menampilkan keluaran dari perintah yang dijalankan
            print("Terjadi kesalahan saat menconfigurasi winehq-archive.key ")
    try: 
        subprocess.run(['sudo', 'wget' , '-NP' , '/etc/apt/sources.list.d/' , 'https://dl.winehq.org/wine-builds/ubuntu/dists/focal/winehq-focal.sources' ], check=True)
        print("download berhasil 3/4")
    except subprocess.CalledProcessError as e:
        if e.output:
            print(e.output.decode())  # Menampilkan keluaran dari perintah yang dijalankan
            print("Terjadi kesalahan saat mendownload sources list winehq ")
    
    try:
        subprocess.run(['sudo', 'apt', 'install', 'wine'], check=True)
        print("Pembaruan paket 4/4")
    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat mengunduh wine", e)

def install_package(package_name):
    try:
        subprocess.run(['sudo', 'apt', 'install', package_name], check=True)
        print("Paket {} berhasil diinstal.".format(package_name))
    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat menginstal paket:", e)

def wineopen():
    try:
        clear_screen()
        subprocess.run(['sudo', 'su'], check=True)
    except subprocess.CalledProcessError as e:
        print("terjadi kesalahan saat ganti ke superuser", e)
    try:
        clear_screen()
        subprocess.run(['winecfg'], check=True)
    except subprocess.CalledProcessError as e:
        print("terjadi kesalahan saat membuka wine", e)
    

def option_two():
    clear_screen()
    print("Wine Menu")
    print("1. wine setup")
    print("2. open Wine config (beta)")

    option = input("Masukkan nomor opsi yang ingin Anda pilih: ")

    if option == '1':
     download_wine()
    elif option == '2':
     wineopen()
    else:
        print("Opsi tidak valid.")


def option_three():
    clear_screen()
    print("berikut adalah link library gdrive kami :")
    print("link : https://drive.google.com/drive/folders/1zMcIPMLzxnekNze9i80Lxv6I7pSkPNjn?usp=drive_link ")




def main():
    
    
    clear_screen()
    if not check_password():
         clear_screen()
         print("wrong, password.")
         print("eror 401")
         print("err 401")
         print("password salah, menutup apps")
         return

    while True:
        clear_screen()

        



        print("""
   ▄███████▄  ▄█  ███▄▄▄▄   ███▄▄▄▄    ▄████████  ▄██████▄  
  ███    ███ ███  ███▀▀▀██▄ ███▀▀▀██▄ ███    ███ ███    ███ 
  ███    ███ ███▌ ███   ███ ███   ███ ███    █▀  ███    ███ 
  ███    ███ ███▌ ███   ███ ███   ███ ███        ███    ███ 
▀█████████▀  ███▌ ███   ███ ███   ███ ███        ███    ███ 
  ███        ███  ███   ███ ███   ███ ███    █▄  ███    ███ 
  ███        ███  ███   ███ ███   ███ ███    ███ ███    ███ 
 ▄████▀      █▀    ▀█   █▀   ▀█   █▀  ████████▀   ▀██████▀  
                                                              
""")
        print("Pilih")
        print("1. Linux Update")
        print("2. Wine")
        print("3. library gdrive ")
        print("4. exit ")

        option = input("Masukkan nomor opsi yang ingin Anda pilih: ")

        if option == '1':
            update_packages()
        elif option == '2':
            option_two()
        elif option == '3':
         option_three()    
        elif option == '4':
            end_apps()
            break
        else:
            print("Opsi tidak valid.")
        
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
