### Introduction
Mia Yulia Nurrizky (HCK006)

## Deployment Link
https://huggingface.co/spaces/miayulia/Lendingkart-FinalProject

# Lendingkart Customer Loan Approval and Segmentation

Pembuatan Model Machine Learning secara Supervised dan Unsupervised untuk mengembangkan model prediksi persetujuan pinjaman yang efektif untuk memprediksi apakah pengajuan pinjaman oleh pelanggan akan disetujui atau tidak, dengan mempertimbangkan variabel yang relevan. Selain itu, kami juga akan melakukan segmentasi pelanggan untuk mengidentifikasi kelompok-kelompok tertentu yang membantu dalam merancang strategi pemasaran yang lebih tepat dan pendekatan yang sesuai agar dapat meningkatkan pendapatan secara signifikan.

## Features
The project includes the following key features:
- Pra-pemrosesan dan eksplorasi data
- Rekayasa dan seleksi fitur
- Pelatihan dan evaluasi model
- Penyajian model menggunakan streamlit
- Antarmuka pengguna interaktif untuk input dan prediksi

## Technologies Used
Proyek ini akan menggunakan berbagai alat dan teknologi, termasuk:
- Bahasa pemrograman Python
- Kerangka kerja pembelajaran mesin (Scikit-learn)
- Teknik pra-pemrosesan data
- Model pembelajaran mesin

# Conclusion 
1. **Loan Approval Prediction:**
   - Dalam proyek ini, metrik yang digunakan untuk evaluasi model adalah `precision`. Ini karena fokus utama adalah meminimalkan kesalahan dalam memprediksi pelanggan yang seharusnya ditolak (False Positive) karena dapat berdampak buruk pada perusahaan.
   - Terdapat ketidakseimbangan distribusi `loan_status` dengan proporsi 60:40 antara calon debitur yang disetujui dan ditolak. Hal ini menunjukkan bahwa masih ada pelanggan yang mengajukan pinjaman tanpa evaluasi yang memadai.
   - Variabel yang berpengaruh signifikan terhadap `loan_status` adalah skor kredit (CIBIL score) dan jangka waktu pinjaman (loan term), yang sejalan dengan analisis EDA.
   - Model Gradient Boosting awal memiliki akurasi 95%, namun setelah tuning berhasil meningkatkan akurasi menjadi 98%, menunjukkan kemampuan model dalam melakukan prediksi yang lebih akurat.

2. **Segmentasi Pelanggan:**
   - Dua kelompok pelanggan (cluster) diidentifikasi, yang disebut Kelas A (Cluster 0) dan Kelas B (Cluster 1).
   - Kelas A memiliki profil keuangan yang lebih kuat dengan pendapatan dan nilai aset yang tinggi, sementara Kelas B memiliki pendapatan dan aset yang lebih rendah.
   - Strategi pemasaran yang direkomendasikan untuk Kelas A adalah penawaran pinjaman dengan jumlah yang lebih besar dan jangka waktu yang lebih singkat. Untuk Kelas B, direkomendasikan strategi pinjaman kecil dengan tenor fleksibel.
   - Penggunaan strategi pemasaran yang disesuaikan untuk masing-masing kelas dapat membantu meningkatkan pendapatan perusahaan secara efektif.

Kesimpulannya, proyek ini berhasil mengembangkan model prediksi persetujuan pinjaman yang akurat dan efektif, serta melakukan segmentasi pelanggan untuk merancang strategi pemasaran yang tepat sasaran. Dengan kombinasi ini, diharapkan perusahaan dapat mengoptimalkan keputusan persetujuan pinjaman dan meningkatkan pendapatan melalui pendekatan yang disesuaikan untuk setiap kelompok pelanggan.
