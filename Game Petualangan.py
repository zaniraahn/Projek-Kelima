import time
import random

def cetak(text=""):
    """Print teks dengan jeda 0.5 detik untuk efek dramatis"""
    print(text)
    time.sleep(0.5)

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
        cetak(f"\n📊 === STATUS PEMAIN: {self.nama} === 📊")
        cetak(f"❤️  Nyawa: {self.nyawa}/{self.max_nyawa}")
        cetak(f"⭐ Level: {self.level} | EXP: {self.exp}/100")
        cetak(f"💰 Gold: {self.gold} | 💎 Diamond: {self.diamond}")
        cetak("-" * 50)
    
    def kurangi_nyawa(self, jumlah):
        """Mengurangi nyawa pemain"""
        self.nyawa -= jumlah
        if self.nyawa < 0:
            self.nyawa = 0
        cetak(f"⚠️  Nyawa berkurang {jumlah}! Sisa nyawa: {self.nyawa}")
    
    def tambah_exp(self, jumlah):
        """Menambah EXP dan cek level up"""
        self.exp += jumlah
        cetak(f"⭐ +{jumlah} EXP")
        
        if self.exp >= 100:
            self.level_up()
    
    def level_up(self):
        """Naik level"""
        self.level += 1
        self.exp = 0
        self.max_nyawa += 20
        self.nyawa = self.max_nyawa
        cetak(f"\n🎉 LEVEL UP! Anda sekarang level {self.level}!")
        cetak(f"❤️  Max nyawa meningkat menjadi {self.max_nyawa}!")
    
    def tambah_reward(self, gold=0, diamond=0):
        """Menambah hadiah"""
        self.gold += gold
        self.diamond += diamond
        if gold > 0:
            cetak(f"💰 +{gold} Gold!")
        if diamond > 0:
            cetak(f"💎 +{diamond} Diamond!")

def tampilkan_intro():
    """Menampilkan intro cerita"""
    cetak("\n" + "="*60)
    cetak("       PETUALANGAN DI DUNIA FANTASI: PULAU MISTERIUS")
    cetak("="*60 + "\n")
    
    cetak("Anda adalah seorang penjelajah pelaut yang berpengalaman.")
    cetak("Memimpin kapal dengan kru setia untuk mencari harta karun.")
    cetak("\nNamun, takdir berkata lain...")
    time.sleep(1)
    cetak("\n⚡ Badai besar menghantam kapal Anda! ⚡")
    cetak("Gelombang besar mendorong kapal menabrak batu karang...")
    cetak("\nKARACK! Kapal Anda karam! 💔")
    cetak("\nAnda berhasil selamat dan terdampar di pantai sebuah pulau misterius.")
    time.sleep(1.5)

def cari_kompas():
    """Pemain menemukan kompas navigasi"""
    cetak("\n" + "-"*60)
    cetak("Setelah berjam-jam berjalan di pantai yang sepi...")
    cetak("Anda menemukan sesuatu di pasir! 🧭")
    time.sleep(1)
    cetak("\nSebuah KOMPAS NAVIGASI kuno dengan cahaya mistis!")
    cetak("Kompas ini menunjukkan koordinat tidak diketahui...")
    cetak("Seperti ada yang menginginkan Anda menemukan sesuatu...")
    time.sleep(1.5)

def pasar_ghaib(stats):
    """Event pasar ghaib untuk bertahan hidup"""
    cetak("\n" + "="*60)
    cetak("✨ MEMASUKI PASAR GHAIB ✨")
    cetak("="*60)
    time.sleep(1)
    
    if stats.gold >= 50 or stats.diamond >= 2:
        cetak(f"\n{stats.nama}, Anda merasa lapar dan kekurangan bahan makanan...")
        time.sleep(1)
        cetak("Tiba-tiba, kabut aneh muncul dan Anda melihat sebuah pasar ghaib!")
        time.sleep(1.5)
        
        cetak("\n🏪 Seorang pedagang misterius mendatangi Anda...")
        cetak("'Halo, penjelajah... Aku memiliki makanan yang bisa menyelamatkanmu!'")
        time.sleep(1)
        
        cetak("\n[1] Beli Makanan dengan Gold (50 Gold → +30 Nyawa)")
        cetak("[2] Beli Makanan dengan Diamond (2 Diamond → +40 Nyawa + 50 Gold)")
        cetak("[3] Tolak dan lanjutkan petualangan (Kurangi 25 nyawa)")
        time.sleep(1)
        
        pilihan = input("\nPilih opsi (1/2/3): ").strip()
        
        if pilihan == "1" and stats.gold >= 50:
            cetak(f"\n{stats.nama} membeli makanan dengan 50 Gold")
            stats.gold -= 50
            stats.nyawa = min(stats.nyawa + 30, stats.max_nyawa)
            cetak("✅ Anda merasa kekuatan kembali!")
            stats.tambah_exp(10)
        elif pilihan == "2" and stats.diamond >= 2:
            cetak(f"\n{stats.nama} membeli makanan premium dengan 2 Diamond")
            stats.diamond -= 2
            stats.nyawa = min(stats.nyawa + 40, stats.max_nyawa)
            stats.gold += 50
            cetak("✅ Makanan lezat memulihkan nyawa Anda sepenuhnya!")
            stats.tambah_exp(20)
        else:
            cetak(f"\n{stats.nama} menolak menawarkan pedagang ghaib...")
            cetak("Tanpa makanan, Anda merasa lemas...")
            stats.kurangi_nyawa(25)
            cetak("⚠️  Pilihan salah akan membuat Anda kelaparan!")
        
        time.sleep(1)
        cetak("\nPasar ghaib mulai menghilang dalam kabut...")
        time.sleep(1)
    else:
        cetak(f"\n{stats.nama}, Anda merasa lapar...")
        cetak("Sebuah pasar ghaib muncul, namun Anda tidak punya uang yang cukup.")
        cetak("Anda harus melanjutkan tanpa makanan...")
        time.sleep(1)
    
def pilih_jalur(nama):
    """Pemilihan jalur petualangan dengan if-else"""
    cetak("\n" + "-"*60)
    cetak(f"Baiklah, {nama}! Kompas navigasi menunjukkan 2 kemungkinan rute:")
    time.sleep(1)
    cetak("\n[1] LAUT LEPAS - Jalur yang terbuka luas, penuh misteri")
    cetak("    Lebih cepat namun lebih berbahaya. Makhluk laut besar berkeliaran.")
    time.sleep(0.5)
    cetak("\n[2] JEJAK KEPITING - Jalur melalui pantai berbatu dan hutan")
    cetak("    Lebih lambat namun lebih aman. Ada jejak misterius di sini.")
    time.sleep(1.5)
    
    cetak("\n" + "-"*60)
    pilihan = input("Pilih jalur mana yang ingin Anda tempuh? (1 atau 2): ").strip()
    
    return pilihan

def jalur_laut_lepas(stats):
    """Rute: Laut Lepas"""
    cetak("\n" + "="*60)
    cetak("🌊 ANDA MEMILIH: LAUT LEPAS 🌊")
    cetak("="*60)
    time.sleep(1)
    
    cetak(f"\n{stats.nama}, Anda berlayar di lautan luas sendirian...")
    time.sleep(1)
    cetak("Ombak besar menggoyangkan kapal kecil yang Anda himpun dari kayu kapal lama.")
    time.sleep(1.5)
    
    # Peristiwa pertama - Kekurangan makanan
    cetak("\n🌊 Anda memasuki perairan yang gelap dan sepi...")
    time.sleep(1)
    cetak("Bekal makanan Anda mulai menipis, perut berbunyi lapar.")
    time.sleep(1)
    pasar_ghaib(stats)
    
    if stats.nyawa <= 0:
        return
    
    time.sleep(2)
    
    cetak("\n⛵ Tiba-tiba! Sebuah kapal berlayar mendatangi Anda!")
    time.sleep(1)
    cetak("Bendera Bajak Laut berkibar di udara...")
    time.sleep(1)
    cetak("Seorang kapten dengan mata patch emas memandang Anda dari kejauhan.")
    time.sleep(1.5)
    
    cetak("\n🏴 KAPTEN BAJAK LAUT: 'SIAPA YANG BERANI MASUK WILAYAH KAMI?'")
    time.sleep(1)
    cetak(f"Kapten berkata: 'Saya adalah Dread Pirate Valdor, penguasa pulau ini!'")
    time.sleep(1)
    cetak("'Kamu tahu, aku tidak pernah membiarkan penyusup pergi begitu saja...'")
    time.sleep(2)

def jalur_jejak_kepiting(stats):
    """Rute: Jejak Kepiting"""
    cetak("\n" + "="*60)
    cetak("🦀 ANDA MEMILIH: JEJAK KEPITING 🦀")
    cetak("="*60)
    time.sleep(1)
    
    cetak(f"\n{stats.nama}, Anda memutuskan berjalan mengikuti jejak kepiting di pasir...")
    time.sleep(1)
    cetak("Jejak itu membawa Anda melewati pantai berbatu dan pohon-pohon aneh.")
    time.sleep(1.5)
    
    # Peristiwa pertama - Kekurangan makanan
    cetak("\n🌙 Malam tiba dan Anda belum menemukan tempat yang aman...")
    time.sleep(1)
    cetak("Kelaparan melanda karena persediaan makanan sangat terbatas.")
    time.sleep(1)
    pasar_ghaib(stats)
    
    if stats.nyawa <= 0:
        return
    
    time.sleep(2)
    
    cetak("\nSetelah berjalan jauh, Anda menemukan sebuah gua! 🕳️")
    time.sleep(1)
    cetak("Di dalam gua terdapat simbol-simbol kuno dan harta karun lama.")
    time.sleep(1.5)
    
    cetak("\n💀 Tiba-tiba, seseorang menghadang Anda dari dalam gua!")
    time.sleep(1)
    cetak("'SIAPA YANG BERANI MENGAMBIL HARTA MILIKKU?'")
    time.sleep(1)
    cetak("Seorang bajak laut dengan tanda luka di wajahnya keluar dari kegelapan.")
    time.sleep(1.5)
    
    cetak("\n🏴 KUMARBI LOKUS (Penguasa Gua):") 
    time.sleep(0.5)
    cetak("'Aku adalah Kumarbi Lokus! Penjaga harta karun pulau ini!'")
    time.sleep(1)
    cetak("'Bayar dengan nyawamu atau dapatkan kekayaan!'")
    time.sleep(2)

def pertarungan(stats, jenis_lawan):
    """Sistem pertarungan dengan musuh"""
    cetak("\n" + "-"*60)
    cetak("⚔️  PERTARUNGAN DIMULAI! ⚔️")
    cetak("-"*60 + "\n")
    
    # Stats awal
    hp_musuh = 80 if jenis_lawan == "laut_lepas" else 75
    nama_musuh = "Dread Pirate Valdor" if jenis_lawan == "laut_lepas" else "Kumarbi Lokus"
    
    putaran = 1
    
    while stats.nyawa > 0 and hp_musuh > 0:
        cetak(f"--- PUTARAN {putaran} ---")
        cetak(f"HP Anda: {stats.nyawa}/{stats.max_nyawa} | HP {nama_musuh}: {hp_musuh}")
        time.sleep(0.5)
        
        # Aksi pemain
        aksi = input("\nPilih aksi: (1) Serang (2) Hindari (3) Penyembuhan: ").strip()
        
        if aksi == "1":
            cetak(f"\n{stats.nama} menyerang dengan pedang! ⚡")
            damage = random.randint(15, 35)
            hp_musuh -= damage
            cetak(f"{nama_musuh} menerima {damage} damage!")
            time.sleep(0.5)
        elif aksi == "2":
            cetak(f"\n{stats.nama} berusaha menghindari serangan musuh! 🛡️")
            time.sleep(0.5)
        elif aksi == "3":
            cetak(f"\n{stats.nama} menggunakan ramuan penyembuhan! 💊")
            heal = random.randint(15, 25)
            stats.nyawa = min(stats.nyawa + heal, stats.max_nyawa)
            cetak(f"HP Anda pulih sebanyak {heal}!")
            time.sleep(0.5)
        else:
            cetak("❌ Aksi tidak valid! Anda terpaksa menerima serangan musuh tanpa perlindungan!")
            cetak("⚠️  Nyawa berkurang 20 karena kesalahan pilihan!")
            stats.kurangi_nyawa(20)
        
        # Aksi musuh
        if hp_musuh > 0:
            musuh_aksi = random.randint(1, 3)
            time.sleep(0.5)
            
            if musuh_aksi == 1:
                cetak(f"{nama_musuh} menyerang balik! 🔥")
                damage = random.randint(8, 20)
                stats.nyawa -= damage
                cetak(f"Anda menerima {damage} damage!")
            elif musuh_aksi == 2:
                cetak(f"{nama_musuh} bersiap untuk serangan lebih kuat!")
            else:
                cetak(f"{nama_musuh} menyembuhkan diri...")
                hp_musuh = min(hp_musuh + 10, 80)
            
            time.sleep(1)
        
        putaran += 1
        cetak()
    
    # Bonusakan EXP jika menang
    if stats.nyawa > 0:
        stats.tambah_exp(50)
    
    return stats.nyawa > 0
    
    # Bonusakan EXP jika menang
    if stats.nyawa > 0:
        stats.tambah_exp(50)
    
    return stats.nyawa > 0

def akhir_cerita(stats, menang, jalur):
    """Menampilkan akhir cerita"""
    cetak("\n" + "="*60)
    
    if menang:
        cetak("🎉 KEMENANGAN! 🎉")
        cetak("="*60)
        time.sleep(1)
        cetak(f"\n{stats.nama}, Anda berhasil mengalahkan musuh Anda!")
        time.sleep(1)
        
        # Jalur Laut Lepas - Reward Gold
        if jalur == "1":
            cetak("\nKapten Bajak Laut Valdor jatuh ke laut...")
            time.sleep(1)
            cetak("Kapalnya menjadi milik Anda!")
            time.sleep(1)
            cetak("\n💰 Anda menemukan harta karun senilai 500 Gold!")
            stats.tambah_reward(gold=500)
            time.sleep(1)
        # Jalur Jejak Kepiting - Reward Diamond
        else:
            cetak("\nKumarbi Lokus tergeletak tak bernyawa di gua...")
            time.sleep(1)
            cetak("Harta karun kuno di gua tersebut kini milik Anda!")
            time.sleep(1)
            cetak("\n💎 Anda menemukan 10 permata langka dan 300 Gold!")
            stats.tambah_reward(gold=300, diamond=10)
            time.sleep(1)
        
        cetak(f"\nDari kapal baru atau harta karun, Anda mampu memulai petualangan baru.")
        time.sleep(1)
        cetak(f"Nama {stats.nama} kini dikenal di seluruh penjuru laut sebagai pemenang!")
        time.sleep(2)
        
        # Tampilkan final stats
        cetak("\n" + "="*60)
        cetak("📊 STATISTIK AKHIR PETUALANGAN")
        cetak("="*60)
        stats.tampilkan_stats()
        
        cetak("\n✨ PETUALANGAN BERAKHIR DENGAN BAIK! ✨")
        
    else:
        cetak("💀 KEKALAHAN! 💀")
        cetak("="*60)
        time.sleep(1)
        cetak(f"\nHP Anda telah habis... {stats.nama} gugur dalam pertarungan demi kehormatan.")
        time.sleep(1)
        
        if jalur == "1":
            cetak("\nKapten Bajak Laut Valdor tertawa mengejek mayat Anda...")
            time.sleep(1)
            cetak("Harta karun yang Anda kejar akan selamanya menjadi rahasia pulau ini.")
        else:
            cetak("\nKumarbi Lokus menambahkan Anda ke daftar penjaga mayat di gua...")
            time.sleep(1)
            cetak("Harta karun tetap bersembunyi dalam kegelapan gua yang mencekam.")
        
        time.sleep(1)
        
        # Tampilkan final stats
        cetak("\n" + "="*60)
        cetak("📊 STATISTIK AKHIR PETUALANGAN")
        cetak("="*60)
        stats.tampilkan_stats()
        
        cetak("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN RUTE BERBEDA! ⚫")
    
    cetak("\n" + "="*60 + "\n")

def game_utama():
    cetak("--- MEMULAI PETUALANGAN DIGITAL ---")
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
            cetak("\n💀 KEKALAHAN! 💀")
            cetak("="*60)
            cetak(f"\n{stats.nama} meninggal kehabisan makanan dan kelaparan...")
            time.sleep(1)
            stats.tampilkan_stats()
            cetak("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN PERSIAPAN LEBIH BAIK! ⚫")
        else:
            menang = pertarungan(stats, "laut_lepas")
            akhir_cerita(stats, menang, jalur)
    
    # Jalur Jejak Kepiting
    elif jalur == "2":
        jalur_jejak_kepiting(stats)
        
        # Check jika nyawa sudah habis di pasar ghaib
        if stats.nyawa <= 0:
            cetak("\n💀 KEKALAHAN! 💀")
            cetak("="*60)
            cetak(f"\n{stats.nama} meninggal kehabisan makanan dan kelaparan...")
            time.sleep(1)
            stats.tampilkan_stats()
            cetak("\n⚫ JANGAN PUTUS ASA! COBA LAGI DENGAN PERSIAPAN LEBIH BAIK! ⚫")
        else:
            menang = pertarungan(stats, "jejak_kepiting")
            akhir_cerita(stats, menang, jalur)
    
    else:
        cetak("❌ Input tidak valid! Permainan berakhir.")
        return
    
    # Opsi bermain lagi
    ulang = input("Ingin bermain lagi? (y/n): ").strip().lower()
    if ulang == 'y':
        game_utama()
    else:
        cetak("\n🌊 Terima kasih telah bermain! Sampai jumpa di petualangan berikutnya! 🌊\n")

if __name__ == "__main__":
    game_utama()
    