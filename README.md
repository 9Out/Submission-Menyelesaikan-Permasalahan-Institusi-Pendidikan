# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

Berdasarkan latar belakang di atas, permasalahan bisnis utama yang harus diselesaikan dalam proyek ini adalah:

1. #### Tingginya angka dropout mahasiswa
3. #### Kesulitan mengidentifikasi mahasiswa yang berisiko dropout
2. #### Pemanfaatan data yang belum optimal
3. #### Kurangnya metode dalam memonitoring performa mahasiswa

### Cakupan Proyek

Untuk menyelesaikan permasalahan bisnis tersebut, cakupan (scope) pada proyek ini meliputi:

- Persiapan & Pembersihan Data (Data Preparation): Melakukan penanganan missing values, penghapusan kolom yang tidak relevan, dan transformasi data tekstual menjadi numerik agar siap diolah.

- Exploratory Data Analysis (EDA): Menganalisis distribusi data untuk menemukan pola awal terkait demografi karyawan dan hubungannya dengan tingkat attrition.

- Pembuatan Business Dashboard: Merancang dasbor interaktif (menggunakan Looker Studio) yang menampilkan metrik utama dan faktor pemicu Dropout untuk mempermudah institusi dalam mengambil keputusan.

- Pembuatan Model Machine Learning: Membangun dan mengevaluasi model klasifikasi (menggunakan algoritma seperti Random Forest, Logistic Regression, dan XGBoost) untuk memprediksi potensi Dropout dan mengekstrak Feature Importance.

- Penyusunan Rekomendasi Bisnis: Memberikan action items yang praktis dan solutif bagi manajemen Jaya Jaya Institut berdasarkan temuan data.

### Persiapan

Sumber data: github link sendiri

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

## Prototype Machine Learning
Link Prototype Machine Learning pada Streamlit Community Cloud:
```

```

## Conclusion

ermasalahan utama di Jaya Jaya Institut berakar pada kurangnya pemanfaatan data secara strategis dalam memonitor dan memprediksi performa mahasiswa.

Dari analisis yang dilakukan, dapat disimpulkan bahwa:

1. Tingginya angka dropout bukan terjadi secara tiba-tiba, tetapi memiliki pola yang dapat dideteksi sejak dini (misalnya dari performa akademik, kehadiran, atau faktor lainnya).

2. Institusi sebenarnya sudah memiliki data yang cukup, namun belum dimanfaatkan secara optimal untuk pengambilan keputusan.

3. Tidak adanya sistem monitoring yang terstruktur menyebabkan pihak kampus terlambat mengidentifikasi mahasiswa berisiko.

4. Tanpa metode prediktif, penanganan masih bersifat reaktif, bukan preventif.

5. Dengan adanya sistem yang menggunakan model xgboost_model.pkl, institusi kini memiliki kemampuan proaktif untuk mengidentifikasi mahasiswa berisiko tinggi sebelum mereka benar-benar keluar, sehingga intervensi dapat dilakukan lebih dini.

### Rekomendasi Action Items (Optional)

Untuk menekan angka Dropout, berikut adalah beberapa action items strategis yang direkomendasikan untuk manajemen Jaya Jaya Institut:

- #### Action Item 1:Implementasi Early Warning System (EWS)

    Bangun sistem untuk mendeteksi mahasiswa berisiko dropout sejak dini.

- #### Action Item 2: Intervensi Dini (Targeted Intervention)
    Setelah mahasiswa berisiko teridentifikasi, lakukan tindakan cepat seperti melakukan konsultasi atau bimbingan konseling dengan mahasiswa terkait.

- #### Action Item 3: Evaluasi Beasiswa dan Dukungan Finansial
    Melakukan peninjauan kembali terhadap distribusi beasiswa. Memberikan bantuan finansial tambahan atau skema cicilan khusus bagi mahasiswa berprestasi yang teridentifikasi memiliki kendala ekonomi agar mereka tidak terhenti di tengah jalan.
