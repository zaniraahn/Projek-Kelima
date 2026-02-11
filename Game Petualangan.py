import time
import random

class StatsPemain:
    """Kelas untuk mengelola status pemain"""
    def __init__(self, nama):
        self.nama = nama
        self.nyawa = 100
        self.max_nyawa = 100
        self.exp = 0
        self.level = 1
        self.gold = 0
        self.diamond = 0
    
    def tampilkan_stats(self):
        """Menampilkan status pemain"""
        print(f"\n📊 === STATUS PEMAIN: {self.nama} === 📊")
        print(f"❤️  Nyawa: {self.nyawa}/{self.max_nyawa}")
        print(f"⭐ Level: {self.level} | EXP: {self.exp}/100")
        print(f"💰 Gold: {self.gold} | 💎 Diamond: {self.diamond}")
        print("-" * 50)
    
    def kurangi_nyawa(self, jumlah):
        """Mengurangi nyawa pemain"""
        self.nyawa -= jumlah
        if self.nyawa < 0:
            self.nyawa = 0
        print(f"⚠️  Nyawa berkurang {jumlah}! Sisa nyawa: {self.nyawa}")
    
    def tambah_exp(self, jumlah):
        """Menambah EXP dan cek level up"""
        self.exp += jumlah
        print(f"⭐ +{jumlah} EXP")
        
        if self.exp >= 100:
            self.level_up()
    
    def level_up(self):
        """Naik level"""
        self.level += 1
        self.exp = 0
        self.max_nyawa += 20
        self.nyawa = self.max_nyawa
        print(f"\n🎉 LEVEL UP! Anda sekarang level {self.level}!")
        print(f"❤️  Max nyawa meningkat menjadi {self.max_nyawa}!")
    
    def tambah_reward(self, gold=0, diamond=0):
        """Menambah hadiah"""
        self.gold += gold
        self.diamond += diamond
        if gold > 0:
            print(f"💰 +{gold} Gold!")
        if diamond > 0:
            print(f"💎 +{diamond} Diamond!")

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

def pasar_ghaib(stats):
    """Event pasar ghaib untuk bertahan hidup"""
    print("\n" + "="*60)
    print("✨ MEMASUKI PASAR GHAIB ✨")
    print("="*60)
    time.sleep(1)
    
    if stats.gold >= 50 or stats.diamond >= 2:
        print(f"\n{stats.nama}, Anda merasa lapar dan kekurangan bahan makanan...")
        time.sleep(1)
        print("Tiba-tiba, kabut aneh muncul dan Anda melihat sebuah pasar ghaib!")
        time.sleep(1.5)
        
        print("\n🏪 Seorang pedagang misterius mendatangi Anda...")
        print("'Halo, penjelajah... Aku memiliki makanan yang bisa menyelamatkanmu!'")
        time.sleep(1)
        
        print("\n[1] Beli Makanan dengan Gold (50 Gold → +30 Nyawa)")
        print("[2] Beli Makanan dengan Diamond (2 Diamond → +40 Nyawa + 50 Gold)")
        print("[3] Tolak dan lanjutkan petualangan (Kurangi 25 nyawa)")
        time.sleep(1)
        
        pilihan = input("\nPilih opsi (1/2/3): ").strip()
        
        if pilihan == "1" and stats.gold >= 50:
            print(f"\n{stats.nama} membeli makanan dengan 50 Gold")
            stats.gold -= 50
            stats.nyawa = min(stats.nyawa + 30, stats.max_nyawa)
            print("✅ Anda merasa kekuatan kembali!")
            stats.tambah_exp(10)
        elif pilihan == "2" and stats.diamond >= 2:
            print(f"\n{stats.nama} membeli makanan premium dengan 2 Diamond")
            stats.diamond -= 2
            stats.nyawa = min(stats.nyawa + 40, stats.max_nyawa)
            stats.gold += 50
            print("✅ Makanan lezat memulihkan nyawa Anda sepenuhnya!")
            stats.tambah_exp(20)
        else:
            print(f"\n{stats.nama} menolak menawarkan pedagang ghaib...")
            print("Tanpa makanan, Anda merasa lemas...")
            stats.kurangi_nyawa(25)
            print("⚠️  Pilihan salah akan membuat Anda kelaparan!")
        
        time.sleep(1)
        print("\nPasar ghaib mulai menghilang dalam kabut...")
        time.sleep(1)
    else:
        print(f"\n{stats.nama}, Anda merasa lapar...")
        print("Sebuah pasar ghaib muncul, namun Anda tidak punya uang yang cukup.")
        print("Anda harus melanjutkan tanpa makanan...")
        time.sleep(1)
    
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

def jalur_laut_lepas(stats):
    """Rute: Laut Lepas"""
    print("\n" + "="*60)
    print("🌊 ANDA MEMILIH: LAUT LEPAS 🌊")
    print("="*60)
    time.sleep(1)
    
    print(f"\n{stats.nama}, Anda berlayar di lautan luas sendirian...")
    time.sleep(1)
    print("Ombak besar menggoyangkan kapal kecil yang Anda himpun dari kayu kapal lama.")
    time.sleep(1.5)
    
    # Peristiwa pertama - Kekurangan makanan
    print("\n🌊 Anda memasuki perairan yang gelap dan sepi...")
    time.sleep(1)
    print("Bekal makanan Anda mulai menipis, perut berbunyi lapar.")
    time.sleep(1)
    pasar_ghaib(stats)
    
    if stats.nyawa <= 0:
        return
    
    time.sleep(2)
    
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

def jalur_jejak_kepiting(stats):
    """Rute: Jejak Kepiting"""
    print("\n" + "="*60)
    print("🦀 ANDA MEMILIH: JEJAK KEPITING 🦀")
    print("="*60)
    time.sleep(1)
    
    print(f"\n{stats.nama}, Anda memutuskan berjalan mengikuti jejak kepiting di pasir...")
    time.sleep(1)
    print("Jejak itu membawa Anda melewati pantai berbatu dan pohon-pohon aneh.")
    time.sleep(1.5)
    
    # Peristiwa pertama - Kekurangan makanan
    print("\n🌙 Malam tiba dan Anda belum menemukan tempat yang aman...")
    time.sleep(1)
    print("Kelaparan melanda karena persediaan makanan sangat terbatas.")
    time.sleep(1)
    pasar_ghaib(stats)
    
    if stats.nyawa <= 0:
        return
    
    time.sleep(2)
    
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

def pertarungan(stats, jenis_lawan):
    """Sistem pertarungan dengan musuh"""
    print("\n" + "-"*60)
    print(f"⚔️  PERTARUNGAN DIMULAI! ⚔️")
    print("-"*60 + "\n")
    
    # Stats awal
    hp_musuh = 80 if jenis_lawan == "laut_lepas" else 75
    nama_musuh = "Dread Pirate Valdor" if jenis_lawan == "laut_lepas" else "Kumarbi Lokus"
    
    putaran = 1
    
    while stats.nyawa > 0 and hp_musuh > 0:
        print(f"--- PUTARAN {putaran} ---")
        print(f"HP Anda: {stats.nyawa}/{stats.max_nyawa} | HP {nama_musuh}: {hp_musuh}")
        time.sleep(0.5)
        
        # Aksi pemain
        aksi = input("\nPilih aksi: (1) Serang (2) Hindari (3) Penyembuhan: ").strip()
        
        if aksi == "1":
            print(f"\n{stats.nama} menyerang dengan pedang! ⚡")
            damage = random.randint(15, 35)
            hp_musuh -= damage
            print(f"{nama_musuh} menerima {damage} damage!")
            time.sleep(0.5)
        elif aksi == "2":
            print(f"\n{stats.nama} berusaha menghindari serangan musuh! 🛡️")
            time.sleep(0.5)
        elif aksi == "3":
            print(f"\n{stats.nama} menggunakan ramuan penyembuhan! 💊")
            heal = random.randint(15, 25)
            stats.nyawa = min(stats.nyawa + heal, stats.max_nyawa)
            print(f"HP Anda pulih sebanyak {heal}!")
            time.sleep(0.5)
        else:
            print("❌ Aksi tidak valid! Anda terpaksa menerima serangan musuh tanpa perlindungan!")
            print("⚠️  Nyawa berkurang 20 karena kesalahan pilihan!")
            stats.kurangi_nyawa(20)
        
        # Aksi musuh
        if hp_musuh > 0:
            musuh_aksi = random.randint(1, 3)
            time.sleep(0.5)
            
            if musuh_aksi == 1:
                print(f"{nama_musuh} menyerang balik! 🔥")
                damage = random.randint(8, 20)
                stats.nyawa -= damage
                print(f"Anda menerima {damage} damage!")
            elif musuh_aksi == 2:
                print(f"{nama_musuh} bersiap untuk serangan lebih kuat!")
            else:
                print(f"{nama_musuh} menyembuhkan diri...")
                hp_musuh = min(hp_musuh + 10, 80)
            
            time.sleep(1)
        
        putaran += 1
        print()
    
    # Bonusakan EXP jika menang
    if stats.nyawa > 0:
        stats.tambah_exp(50)
    
    return stats.nyawa > 0

def akhir_cerita(stats, menang, jalur):
    """Menampilkan akhir cerita"""
    print("\n" + "="*60)
    
    if menang:
        print("🎉 KEMENANGAN! 🎉")
        print("="*60)
        time.sleep(1)
        print(f"\n{stats.nama}, Anda berhasil mengalahkan musuh Anda!")
        time.sleep(1)
        
        # Jalur Laut Lepas - Reward Gold
        if jalur == "1":
            print("\nKapten Bajak Laut Valdor jatuh ke laut...")
            time.sleep(1)
            print("Kapalnya menjadi milik Anda!")
            time.sleep(1)
            print("\n💰 Anda menemukan harta karun senilai 500 Gold!")
            stats.tambah_reward(gold=500)
            time.sleep(1)
        # Jalur Jejak Kepiting - Reward Diamond
        else:
            print("\nKumarbi Lokus tergeletak tak bernyawa di gua...")
            time.sleep(1)
            print("Harta karun kuno di gua tersebut kini milik Anda!")
            time.sleep(1)
            print("\n💎 Anda menemukan 10 permata langka dan 300 Gold!")
            stats.tambah_reward(gold=300, diamond=10)
            time.sleep(1)
        
        print(f"\nDari kapal baru atau harta karun, Anda mampu memulai petualangan baru.")
        time.sleep(1)
        print(f"Nama {stats.nama} kini dikenal di seluruh penjuru laut sebagai pemenang!")
        time.sleep(2)
        
        # Tampilkan final stats
        print("\n" + "="*60)
        print("📊 STATISTIK AKHIR PETUALANGAN")
        print("="*60)
        stats.tampilkan_stats()
        
        print("\n✨ PETUALANGAN BERAKHIR DENGAN BAIK! ✨")
        
    else:
        print("💀 KEKALAHAN! 💀")
        print("="*60)
        time.sleep(1)
        print(f"\nHP Anda telah habis... {stats.nama} gugur dalam pertarungan demi kehormatan.")
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
        
        # Tampilkan final stats
        print("\n" + "="*60)
        print("📊 STATISTIK AKHIR PETUALANGAN")
        print("="*60)
        stats.tampilkan_stats()
        
        print("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN RUTE BERBEDA! ⚫")
    
    print("\n" + "="*60 + "\n")

def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu, penjelajah? ")
    time.sleep(1)
    
    # Buat object stats pemain
    stats = StatsPemain(nama)
    
    # Menampilkan intro cerita
    tampilkan_intro()
    
    # Pemain menemukan kompas
    cari_kompas()
    
    # Tampilkan stats awal
    stats.tampilkan_stats()
    
    # Pemilihan jalur
    input("\nTekan ENTER untuk melanjutkan...")
    jalur = pilih_jalur(nama)
    
    # Jalur Laut Lepas
    if jalur == "1":
        jalur_laut_lepas(stats)
        
        # Check jika nyawa sudah habis di pasar ghaib
        if stats.nyawa <= 0:
            print("\n💀 KEKALAHAN! 💀")
            print("="*60)
            print(f"\n{stats.nama} meninggal kehabisan makanan dan kelaparan...")
            time.sleep(1)
            stats.tampilkan_stats()
            print("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN PERSIAPAN LEBIH BAIK! ⚫")
        else:
            menang = pertarungan(stats, "laut_lepas")
            akhir_cerita(stats, menang, jalur)
    
    # Jalur Jejak Kepiting
    elif jalur == "2":
        jalur_jejak_kepiting(stats)
        
        # Check jika nyawa sudah habis di pasar ghaib
        if stats.nyawa <= 0:
            print("\n💀 KEKALAHAN! 💀")
            print("="*60)
            print(f"\n{stats.nama} meninggal kehabisan makanan dan kelaparan...")
            time.sleep(1)
            stats.tampilkan_stats()
            print("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN PERSIAPAN LEBIH BAIK! ⚫")
        else:
            menang = pertarungan(stats, "jejak_kepiting")
            akhir_cerita(stats, menang, jalur)
    
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
    