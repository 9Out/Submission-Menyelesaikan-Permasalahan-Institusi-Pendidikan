# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Berdasarkan latar belakang di atas, permasalahan bisnis utama yang harus diselesaikan dalam proyek ini adalah:

1. #### Tingginya proporsi siswa yang berakhir Dropout berisiko menurunkan angka kelulusan serta membuat intervensi retensi menjadi terlambat dan kurang tepat sasaran.

2. #### Institusi masih kesulitan mengenali faktor akademik dan administratif yang paling kuat membedakan siswa yang berakhir Dropout dan Graduate, sehingga prioritas penanganan belum berbasis data.

3. #### Institusi belum memiliki sarana monitoring dan prototipe prediksi yang dapat membantu staf akademik membaca risiko siswa lebih dini dan mengambil tindakan yang lebih terarah.


### Cakupan Proyek

Untuk menyelesaikan permasalahan bisnis tersebut, cakupan (scope) pada proyek ini meliputi:

- Persiapan & Pembersihan Data (Data Preparation): Melakukan penanganan missing values, penghapusan kolom yang tidak relevan, dan transformasi data tekstual menjadi numerik agar siap diolah.

- Exploratory Data Analysis (EDA): Menganalisis distribusi data untuk menemukan pola awal terkait demografi karyawan dan hubungannya dengan tingkat attrition.

- Pembuatan Business Dashboard: Merancang dasbor interaktif (menggunakan Looker Studio) yang menampilkan metrik utama dan faktor pemicu Dropout untuk mempermudah institusi dalam mengambil keputusan.

- Pembuatan Model Machine Learning: Membangun dan mengevaluasi model klasifikasi (menggunakan algoritma seperti Random Forest, Logistic Regression, dan XGBoost) untuk memprediksi potensi Dropout dan mengekstrak Feature Importance.

- Penyusunan Rekomendasi Bisnis: Memberikan action items yang praktis dan solutif bagi manajemen Jaya Jaya Institut berdasarkan temuan data.

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv]

Setup environment:

1. Buat dan aktifkan virtual environment (opsional)
```
python -m venv venv
source venv/bin/activate  # Gunakan 'venv\Scripts\activate' jika di Windows
```

2. Install dependencies
```
pip install -r requirements.txt
```

## Business Dashboard

Dashboard dibangun menggunakan Looker Studio dan mencakup:

- Jumlah Mahasiswa
- Jumlah Penerima Beasiswa
- Jumlah Mahasiswa yang berhutang
- Jenis Mahasiswa menurut Status
- Penggolongan Umur Mahasiswa menurut Status
- Penerima Beasiswa menurut Status
- Mahasiswa yang Memiliki Hutang menurut Status
- Pembayaran Biaya Kuliah menurut Status

### Link File Dashboard
```
https://datastudio.google.com/reporting/eb7cfde7-3f28-4324-98ea-a34bc53ece81
```

## Menjalankan Sistem Machine Learning

Langkah menjalankan sistem secara lokal:
```
- Pastikan Sudah menginstall seluruh requirements yang dibutuhkan.

- Jalankan sistem, streamlit run app.py
```

Link Sistem Machine Learning pada Streamlit Community Cloud:
```
https://sistem-prediksi-dropout-institut.streamlit.app/
```

## Conclusion

Proyek ini menunjukkan bahwa masalah dropout di Jaya Jaya Institut paling kuat berkaitan dengan kombinasi performa akademik awal dan kedisiplinan administrasi siswa. Dengan memfokuskan analisis pada perbedaan antara siswa yang berakhir Dropout dan Graduate, project ini membantu institusi menjawab tiga kebutuhan utama: mengenali faktor risiko yang paling penting, memonitor kelompok yang paling rentan melalui dashboard, dan menyediakan prototipe prediksi yang siap dipakai untuk triase awal.

Dari analisis yang dilakukan, dapat disimpulkan bahwa:

1. Dataset sumber asli dari Dicoding berisi 4.424 siswa tanpa missing value dan tanpa data duplikat. Untuk submission ini digunakan dataset final berisi 3.630 siswa dengan status akhir Dropout dan Graduate, sehingga seluruh analisis, dashboard, dan pemodelan konsisten pada cakupan proyek yang sama.

2. Model terbaik adalah Logistic Regression dengan accuracy 0,9160 dan weighted f1-score 0,9150.

3. Faktor paling berpengaruh terhadap prediksi status siswa adalah `Curricular_units_2nd_sem_approved`, `Curricular_units_1st_sem_approved`, `Curricular_units_2nd_sem_enrolled`, `Tuition_fees_up_to_date`, dan `Curricular_units_1st_sem_enrolled`.
4. Analisis lanjutan pada notebook juga menyiapkan evaluasi kelompok, sehingga model tidak hanya dilihat dari performa umum tetapi juga dari perilaku risiko pada subset tertentu seperti gender dan kelompok usia.


### Rekomendasi Action Items (Optional)

Untuk menekan angka Dropout, berikut adalah beberapa action items strategis yang direkomendasikan untuk manajemen Jaya Jaya Institut:

- #### Action Item 1:Implementasi Early Warning System (EWS)

    Bangun sistem peringatan dini yang menandai siswa dengan `Curricular_units_2nd_sem_approved <= 2` sebagai kandidat intervensi akademik paling mendesak. Rata-rata siswa `Dropout` hanya menyelesaikan `1,94` mata kuliah pada semester kedua, jauh di bawah kelompok `Graduate` yang berada di `6,18`, sehingga ambang ini dapat dipakai sebagai trigger awal untuk mentoring wajib, kelas remedial, dan review rencana studi dalam `1-2` minggu setelah nilai semester keluar.

- #### Action Item 2: Intervensi Dini (Targeted Intervention)
    Gabungkan intervensi akademik dan finansial untuk siswa dengan `Tuition_fees_up_to_date = 0`. Pada data final, kelompok dengan pembayaran tidak mutakhir memiliki `457` kasus dropout dari `486` siswa atau sekitar `94,0%`, sehingga institusi dapat membuat daftar pantauan harian lintas akademik-keuangan, menawarkan skema cicilan atau bantuan darurat, lalu memeriksa kembali progres akademik mereka pada bulan yang sama. 
    
    Fokuskan program retensi pada siswa usia masuk `25 tahun ke atas`, terutama kelompok `25-29` dengan dropout rate `70,2%` dan kelompok `30+` dengan dropout rate `61,4%`. Implementasi praktisnya dapat berupa mentoring singkat, jadwal konsultasi di luar jam kerja, kelas malam, atau kanal dukungan daring yang lebih fleksibel untuk segmen nontradisional ini.

- #### Action Item 3
    Gunakan prototipe machine learning sebagai alat triase untuk membedakan siswa yang pola akademik-awalnya lebih dekat ke `Dropout` atau `Graduate`. Siswa yang memperoleh probabilitas `Dropout` tinggi dan juga berada pada ambang approved units semester dua yang rendah harus diprioritaskan untuk intervensi paling awal.
n