<img width="800" height="250" alt="image" src="https://github.com/user-attachments/assets/d5726028-c080-44ba-9d5c-d63824711fec" />


📌 Tentang Proyek  
RencanaKita adalah sistem rekomendasi investasi yang dirancang untuk membantu user menentukan produk investasi yang paling sesuai berdasarkan profil risiko, tujuan keuangan, serta jangka waktu investasi yang dimiliki.

📖 Latar Belakang  
Investasi menjadi salah satu langkah penting untuk mencapai tujuan finansial di masa depan, seperti dana pendidikan, dana darurat, pembelian rumah, hingga persiapan pensiun. Namun, dalam praktiknya, banyak investor pemula yang belum memahami hubungan antara profil risiko, horizon investasi, dan produk investasi yang mereka pilih.

Sering kali user hanya mengetahui tujuan mereka secara umum, misalnya ingin menabung untuk masa depan atau mencari instrumen investasi yang aman. Akan tetapi, mereka belum tentu memahami apakah produk seperti deposito, SBN, reksa dana, atau saham sesuai dengan toleransi risiko dan kondisi finansial mereka. Hal ini dapat menyebabkan pemilihan instrumen yang kurang tepat, panic selling saat pasar turun, atau bahkan kegagalan mencapai target keuangan jangka panjang.

🎯 Tujuan Proyek  
Proyek ini bertujuan membangun sistem rekomendasi investasi yang dapat membantu user memilih produk investasi sesuai dengan profil risiko, tujuan keuangan, dan jangka waktu investasi, sehingga keputusan investasi menjadi lebih terarah, personal, dan relevan.

📊 Dataset  
Sumber Dataset : Synthetic Data / Internal User Survey

Kolom | Deskripsi
--- | ---
user_age | Usia pengguna
monthly_income | Pendapatan bulanan pengguna
risk_tolerance | Skor toleransi risiko user
investment_horizon | Jangka waktu investasi dalam tahun
investment_goal | Tujuan investasi user
recommended_product | Produk investasi yang direkomendasikan

🧠 Metode  
Risk Profiling  
Classification Model  
Recommendation Engine  
Data Preprocessing  
Content-Based Recommendation

🛠️ Tech Stack  
Library : Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn  
Data Engineering : Airflow, Docker  
Visualization : Tableau / Looker Studio  
Deployment : Streamlit / HuggingFace  

🖥️ Output Proyek  
RencanaKita Dashboard  
RencanaKita App  

📂 Struktur Proyek  
main/  
├── Data Analysis/  
│   ├── Dashboard_url.txt  
│   └── Data_Analysis_RencanaKita.ipynb  
│  
├── Data Engineer/  
│   ├── dags/  
│   │   ├── DAG.py  
│   │   ├── investment_data_clean.csv  
│   │   └── investment_data_raw.csv  
│   │  
│   ├── .env  
│   └── airflow_rencanakita.yaml  
│  
├── Data Science/  
│   └── Data_Science_RencanaKita.ipynb  
│  
├── README.md  
└── RencanaKita.png  

🤝 Tim  
FTDS Batch 039 — Hacktiv8 | Group 001  

Nama | Peran
--- | ---
Aulia Putri | Data Engineer — ETL Pipeline & Airflow
Yosia Oscar Stephen Marpaung | Data Engineer — Deployment & Data Validation
Yehezkiel Erickson Rivaldo P | Data Scientist — Risk Profiling & Recommendation System
Gugun Gunawan | Data Analyst — EDA, Business Insight, & Dashboard


