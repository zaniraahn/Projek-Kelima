import time
import random

def tampilkan_intro():
    """Menampilkan intro cerita"""
    print("\n" + "="*60)
    print("       PETUALANGAN DI DUNIA FANTASI: PULAU MISTERIUS")
    print("="*60 + "\n")
    time.sleep(1)
    
    print("Anda adalah seorang penjelajah pelaut yang berpengalaman.")
    time.sleep(1)
    print("Memimpin kapal dengan kru setia untuk mencari harta karun.")
    time.sleep(1)
    print("\nNamun, takdir berkata lain...")
    time.sleep(1.5)
    print("\n⚡ Badai besar menghantam kapal Anda! ⚡")
    time.sleep(1)
    print("Gelombang besar mendorong kapal menabrak batu karang...")
    time.sleep(1)
    print("\nKARACK! Kapal Anda karam! 💔")
    time.sleep(1)
    print("\nAnda berhasil selamat dan terdampar di pantai sebuah pulau misterius.")
    time.sleep(2)

def cari_kompas():
    """Pemain menemukan kompas navigasi"""
    print("\n" + "-"*60)
    print("Setelah berjam-jam berjalan di pantai yang sepi...")
    time.sleep(1)
    print("Anda menemukan sesuatu di pasir! 🧭")
    time.sleep(1.5)
    print("\nSebuah KOMPAS NAVIGASI kuno dengan cahaya mistis!")
    time.sleep(1)
    print("Kompas ini menunjukkan koordinat tidak diketahui...")
    time.sleep(1)
    print("Seperti ada yang menginginkan Anda menemukan sesuatu...")
    time.sleep(2)

def pilih_jalur(nama):
    """Pemilihan jalur petualangan dengan if-else"""
    print("\n" + "-"*60)
    print(f"Baiklah, {nama}! Kompas navigasi menunjukkan 2 kemungkinan rute:")
    time.sleep(1)
    print("\n[1] LAUT LEPAS - Jalur yang terbuka luas, penuh misteri")
    print("    Lebih cepat namun lebih berbahaya. Makhluk laut besar berkeliaran.")
    time.sleep(0.5)
    print("\n[2] JEJAK KEPITING - Jalur melalui pantai berbatu dan hutan")
    print("    Lebih lambat namun lebih aman. Ada jejak misterius di sini.")
    time.sleep(1.5)
    
    print("\n" + "-"*60)
    pilihan = input("Pilih jalur mana yang ingin Anda tempuh? (1 atau 2): ").strip()
    
    return pilihan

def jalur_laut_lepas(nama):
    """Rute: Laut Lepas"""
    print("\n" + "="*60)
    print("🌊 ANDA MEMILIH: LAUT LEPAS 🌊")
    print("="*60)
    time.sleep(1)
    
    print(f"\n{nama}, Anda berlayar di lautan luas sendirian...")
    time.sleep(1)
    print("Ombak besar menggoyangkan kapal kecil yang Anda himpun dari kayu kapal lama.")
    time.sleep(1.5)
    
    print("\n⛵ Tiba-tiba! Sebuah kapal berlayar mendatangi Anda!")
    time.sleep(1)
    print("Bendera Bajak Laut berkibar di udara...")
    time.sleep(1)
    print("Seorang kapten dengan mata patch emas memandang Anda dari kejauhan.")
    time.sleep(1.5)
    
    print("\n🏴 KAPTEN BAJAK LAUT: 'SIAPA YANG BERANI MASUK WILAYAH KAMI?'")
    time.sleep(1)
    print(f"Kapten berkata: 'Saya adalah Dread Pirate Valdor, penguasa pulau ini!'")
    time.sleep(1)
    print("'Kamu tahu, aku tidak pernah membiarkan penyusup pergi begitu saja...'")
    time.sleep(2)

def jalur_jejak_kepiting(nama):
    """Rute: Jejak Kepiting"""
    print("\n" + "="*60)
    print("🦀 ANDA MEMILIH: JEJAK KEPITING 🦀")
    print("="*60)
    time.sleep(1)
    
    print(f"\n{nama}, Anda memutuskan berjalan mengikuti jejak kepiting di pasir...")
    time.sleep(1)
    print("Jejak itu membawa Anda melewati pantai berbatu dan pohon-pohon aneh.")
    time.sleep(1.5)
    
    print("\nSetelah berjalan jauh, Anda menemukan sebuah gua! 🕳️")
    time.sleep(1)
    print("Di dalam gua terdapat simbol-simbol kuno dan harta karun lama.")
    time.sleep(1.5)
    
    print("\n💀 Tiba-tiba, seseorang menghadang Anda dari dalam gua!")
    time.sleep(1)
    print("'SIAPA YANG BERANI MENGAMBIL HARTA MILIKKU?'")
    time.sleep(1)
    print("Seorang bajak laut dengan tanda luka di wajahnya keluar dari kegelapan.")
    time.sleep(1.5)
    
    print("\n🏴 KUMARBI LOKUS (Penguasa Gua):") 
    time.sleep(0.5)
    print("'Aku adalah Kumarbi Lokus! Penjaga harta karun pulau ini!'")
    time.sleep(1)
    print("'Bayar dengan nyawamu atau dapatkan kekayaan!'")
    time.sleep(2)

def pertarungan(nama, jenis_lawan):
    """Sistem pertarungan dengan musuh"""
    print("\n" + "-"*60)
    print(f"⚔️  PERTARUNGAN DIMULAI! ⚔️")
    print("-"*60 + "\n")
    
    # Stats awal
    hp_pemain = 100
    hp_musuh = 80 if jenis_lawan == "laut_lepas" else 75
    serangan_pemain = random.randint(15, 30)
    serangan_musuh = random.randint(10, 25)
    
    putaran = 1
    
    while hp_pemain > 0 and hp_musuh > 0:
        print(f"--- PUTARAN {putaran} ---")
        print(f"HP Anda: {hp_pemain} | HP Musuh: {hp_musuh}")
        time.sleep(0.5)
        
        # Aksi pemain
        aksi = input("\nPilih aksi: (1) Serang (2) Hindari (3) Penyembuhan: ").strip()
        
        if aksi == "1":
            print(f"\n{nama} menyerang dengan pedang! ⚡")
            damage = random.randint(15, 35)
            hp_musuh -= damage
            print(f"Musuh menerima {damage} damage!")
            time.sleep(0.5)
        elif aksi == "2":
            print(f"\n{nama} berusaha menghindari serangan musuh! 🛡️")
            serangan_musuh = random.randint(5, 15)
            time.sleep(0.5)
        elif aksi == "3":
            print(f"\n{nama} menggunakan ramuan penyembuhan! 💊")
            heal = random.randint(15, 25)
            hp_pemain = min(hp_pemain + heal, 100)
            print(f"HP Anda pulih sebanyak {heal}!")
            time.sleep(0.5)
        else:
            print("Aksi tidak valid! Anda terpaksa menerima serangan musuh!")
        
        # Aksi musuh
        if hp_musuh > 0:
            musuh_aksi = random.randint(1, 3)
            time.sleep(0.5)
            
            if musuh_aksi == 1:
                print(f"Musuh menyerang balik! 🔥")
                damage = random.randint(8, 20)
                hp_pemain -= damage
                print(f"Anda menerima {damage} damage!")
            elif musuh_aksi == 2:
                print(f"Musuh bersiap untuk serangan lebih kuat!")
            else:
                print(f"Musuh meyembuhkan diri...")
                hp_musuh = min(hp_musuh + 10, 80)
            
            time.sleep(1)
        
        putaran += 1
        print()
    
    return hp_pemain > 0

def akhir_cerita(nama, menang, jalur):
    """Menampilkan akhir cerita"""
    print("\n" + "="*60)
    
    if menang:
        print("🎉 KEMENANGAN! 🎉")
        print("="*60)
        time.sleep(1)
        print(f"\n{nama}, Anda berhasil mengalahkan musuh Anda!")
        time.sleep(1)
        
        if jalur == "1":
            print("\nKapten Bajak Laut Valdor jatuh ke laut...")
            time.sleep(1)
            print("Kapalnya menjadi milik Anda!")
            time.sleep(1)
            print("\n💰 Anda menemukan harta karun senilai 10 juta emas!")
            time.sleep(1)
        else:
            print("\nKumarbi Lokus tergeletak tak bernyawa di gua...")
            time.sleep(1)
            print("Harta karun kuno di gua tersebut kini milik Anda!")
            time.sleep(1)
            print("\n💎 Anda menemukan 50 permata langka dan emas murni!")
            time.sleep(1)
        
        print(f"\nDari kapal baru atau harta karun, Anda mampu memulai petualangan baru.")
        time.sleep(1)
        print(f"Nama {nama} kini dikenal di seluruh penjuru laut sebagai pemenang!")
        time.sleep(1)
        print("\n✨ PETUALANGAN BERAKHIR DENGAN BAIK! ✨")
        
    else:
        print("💀 KEKALAHAN! 💀")
        print("="*60)
        time.sleep(1)
        print(f"\nHP Anda telah habis... {nama} gugur dalam pertarungan demi kehormatan.")
        time.sleep(1)
        
        if jalur == "1":
            print("\nKapten Bajak Laut Valdor tertawa mengejek mayat Anda...")
            time.sleep(1)
            print("Harta karun yang Anda kejar akan selamanya menjadi rahasia pulau ini.")
        else:
            print("\nKumarbi Lokus menambahkan Anda ke daftar penjaga mayat di gua...")
            time.sleep(1)
            print("Harta karun tetap bersembunyi dalam kegelapan gua yang mencekam.")
        
        time.sleep(1)
        print("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN RUTE BERBEDA! ⚫")
    
    print("\n" + "="*60 + "\n")

def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu, penjelajah? ")
    time.sleep(1)
    
    # Menampilkan intro cerita
    tampilkan_intro()
    
    # Pemain menemukan kompas
    cari_kompas()
    
    # Pemilihan jalur
    input("\nTekan ENTER untuk melanjutkan...")
    jalur = pilih_jalur(nama)
    
    # Jalur Laut Lepas
    if jalur == "1":
        jalur_laut_lepas(nama)
        menang = pertarungan(nama, "laut_lepas")
        akhir_cerita(nama, menang, jalur)
    
    # Jalur Jejak Kepiting
    elif jalur == "2":
        jalur_jejak_kepiting(nama)
        menang = pertarungan(nama, "jejak_kepiting")
        akhir_cerita(nama, menang, jalur)
    
    else:
        print("❌ Input tidak valid! Permainan berakhir.")
        return
    
    # Opsi bermain lagi
    ulang = input("Ingin bermain lagi? (y/n): ").strip().lower()
    if ulang == 'y':
        game_utama()
    else:
        print("\n🌊 Terima kasih telah bermain! Sampai jumpa di petualangan berikutnya! 🌊\n")

if __name__ == "__main__":
    game_utama()
    