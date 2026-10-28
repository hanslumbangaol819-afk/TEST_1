
def main():
    print("=== Program Python Sederhana ===")
    
    nama = input("Masukkan nama Anda: ")
    print(f"Halo, {nama}! Selamat datang!")
    
    print("\n--- Kalkulator Dasar ---")
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        operasi = input("Pilih operasi (+, -, *, /): ")
        angka2 = float(input("Masukkan angka kedua: "))
        
        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                print("Error: Pembagian dengan nol!")
                return
        else:
            print("Operasi tidak valid!")
            return
        
        print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")
    
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    
    print("\nTerima kasih!")

if __name__ == "__main__":
    main()