def hitung_nilai_rata_rata():
    print("--- Program Input Nilai Mata Kuliah ---")
    

    nama_mahasiswa = input("Masukkan nama: ")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    
    total_nilai = 0
    
    for i in range(jumlah_matkul):
        
        nilai_input = float(input(f"Masukkan nilai mata kuliah ke-{i + 1}: "))
        total_nilai = total_nilai + nilai_input
        
    
    hasil_rata_rata = total_nilai / jumlah_matkul
    
    print("\n--- Hasil Perhitungan ---")
    print("Nama Mahasiswa :", nama_mahasiswa)
    print("Total Nilai    :", total_nilai)
    print("Nilai Rata-rata:", hasil_rata_rata)
    

    if hasil_rata_rata >= 80:
        grade_akhir = "A"
    elif hasil_rata_rata >= 70:
        grade_akhir = "B"
    elif hasil_rata_rata >= 60:
        grade_akhir = "C"
    else:
        grade_akhir = "D atau E"
        
    print("Grade Akhir    :", grade_akhir)

hitung_nilai_rata_rata()