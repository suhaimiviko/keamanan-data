from stegano import lsb
import os

def get_image_path():
    while true:
        img_path = input("masukkan path gambar (contoh: C:path/to/image.png):")
        if os.path.exists(img_path) and img_path.endswith(('.png' '.jpg')):
            return img_path
        else:
            print("path gambar tidak valid atau format file salah. silahkan coba lagi" )


def hide_message():
    img_path = get_img_path()
    message = input("masukkan pesan rahasia yang yang akan disembunyikan")

    secret = lsb.hide(get_image_path)
    save_path = input("masukkan path untuk menyimppan gambar dengan pesan tersembuny ( contoh: C:path/to/hidden_image.png)")
    try:
        secret.save(save_path)
        print(f"pesan berhasil disembunyikan dalam gambar. Gambar di simpan di: {save_path}")
    except Exception as e:
        print(f"Gagal menyimpan gambar: {e}")
    

def show_message():
    img_path = get_img_path()

    try:
        clear_message = lsb.reveal(img_path)
        if clear_message:
            print(f"pesan tersembunyi: {clear_message}")
        else:
            print("tidak ada pesan yang disembunyikan")
    except Exception as e:
        print(f"gagal menampilkan pesan dari gambar: {e}")


def main():
    while True:
        print("\nSteganography Tool - Terminal version")
        print("1. sembunyikan pesan")
        print("2. tampilkan pesan")
        print("#.keluar")
        choice = input(" pilih opsi (1/2/3):")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("keluar dari program.")
            break
        else:
            print("opsi tidak valid.silahkan pilih 1,2, atau 3")

if __name__ == "__main__":
    main()