def diagnosa_ai(gejala):
    # Mengubah input menjadi huruf kecil agar mudah dicek
    g = gejala.lower()
    
    # 1. Penyakit pada Padi
    if "padi" in g and "merah" in g:
        return "Penyakit: Tungro. Solusi: Kendalikan wereng hijau sebagai pembawa virus."
    elif "padi" in g and "busuk" in g and "leher" in g:
        return "Penyakit: Blas (Pyricularia oryzae). Solusi: Semprot fungisida dosis rendah."
    
    # 2. Penyakit pada Jagung
    elif "jagung" in g and "putih" in g and "memanjang" in g:
        return "Penyakit: Bulai. Solusi: Cabut tanaman yang terinfeksi agar tidak menular."
    
    # 3. Penyakit Umum (Daun/Batang)
    elif "daun" in g and "bolong" in g:
        return "Masalah: Hama Ulat/Serangga. Solusi: Gunakan pestisida nabati (daun mimba/nimba)."
    elif "daun" in g and "putih" in g and "tepung" in g:
        return "Penyakit: Embun Tepung. Solusi: Semprotkan campuran air dan soda kue (dosis kecil)."
    elif "akar" in g and "bengkak" in g:
        return "Penyakit: Nematoda Akar. Solusi: Berikan nematisida atau perbaiki drainase tanah."
    elif "buah" in g and "busuk" in g and "hitam" in g:
        return "Penyakit: Antraknosa. Solusi: Kurangi kelembaban dan buang buah yang terinfeksi."
    
    # 4. Masalah Nutrisi (Pupuk)
    elif "daun" in g and "kuning" in g and "bawah" in g:
        return "Defisiensi: Kurang Nitrogen (N). Solusi: Tambahkan pupuk Urea atau kompos."
    elif "daun" in g and "ungu" in g:
        return "Defisiensi: Kurang Fosfor (P). Solusi: Tambahkan pupuk SP-36."
    
    else:
        return "Maaf, AI belum mengenali gejala ini. Coba tulis: 'daun kuning' atau 'padi merah'."

# --- Bagian Uji Coba ---
print("=== ASISTEN AI PERTANIAN SMART ===")
tanya = "padi saya berwarna merah" # Simulasi input petani
print(f"User: {tanya}")
print(f"AI: {diagnosa_ai(tanya)}")
