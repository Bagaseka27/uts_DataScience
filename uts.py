from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Memastikan folder static/images tersedia
IMAGE_FOLDER = os.path.join('static', 'images')
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/')
def index():
    # 1. Load Dataset (Poin 2 UTS)
    # Ganti dengan nama file CSV kamu yang sebenarnya
    dataset_name = 'sleep_health_and_lifestyle_dataset.csv' 
    df = pd.read_csv(dataset_name)

    # =========================================================================
    # --- BAGIAN DATA APA ADANYA ---
    # Kita GUNAKAN DataFrame 'df' langsung, TANPA proses cleaning.
    # Data missing dan outlier akan dibiarkan apa adanya.
    # =========================================================================

    # 2. Statistik Deskriptif (Poin 4 UTS) - Dari Data Apa Adanya
    # Kita tampilkan statistik deskriptif dari data asli.
    stats = df.describe().reset_index().to_html(classes='table table-hover table-bordered table-striped', index=False)

    # 3. Visualisasi Data (Poin 5 UTS) - Dari Data Apa Adanya
    # Matplotlib akan otomatis mengabaikan data missing (NaN) saat membuat grafik.

    # Grafik 1: Histogram Durasi Tidur (Sleep Duration)
    plt.figure(figsize=(8, 5))
    # Kita plot kolom 'Sleep Duration' apa adanya
    plt.hist(df['Sleep Duration'].dropna(), bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribusi Durasi Tidur (Data Apa Adanya)')
    plt.xlabel('Jam')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y', alpha=0.5)
    
    # Simpan grafik
    plot_sleep_path = os.path.join(IMAGE_FOLDER, 'grafik_sleep_as_is.png')
    plt.savefig(plot_sleep_path)
    plt.close()

    # Grafik 2: Bar Chart Rata-rata Kualitas Tidur per Gender
    plt.figure(figsize=(8, 5))
    # Kita hitung rata-rata apa adanya, data missing diabaikan
    df_grouped_gender = df.groupby('Gender')['Quality of Sleep'].mean()
    df_grouped_gender.plot(kind='bar', color=['pink', 'lightgreen'])
    plt.title('Rata-rata Kualitas Tidur Berdasarkan Gender (Data Apa Adanya)')
    plt.ylabel('Skor Kualitas (1-10)')
    plt.xticks(rotation=0) # Agar tulisan 'Female', 'Male' tidak miring
    plt.grid(axis='y', alpha=0.5)

    # Simpan grafik
    plot_gender_path = os.path.join(IMAGE_FOLDER, 'grafik_gender_as_is.png')
    plt.savefig(plot_gender_path)
    plt.close()

    # Grafik 3: Scatter Plot Tekanan Darah vs Durasi Tidur (Contoh visualisasi outlier)
    # Ini bagus untuk melihat outlier secara visual
    plt.figure(figsize=(8, 5))
    # Kita plot kolom 'Blood Pressure' dan 'Sleep Duration' apa adanya
    plt.scatter(df['Sleep Duration'], df['Blood Pressure'], color='purple', alpha=0.5)
    plt.title('Scatter Plot: Durasi Tidur vs Tekanan Darah (Data Apa Adanya)')
    plt.xlabel('Durasi Tidur (Jam)')
    plt.ylabel('Tekanan Darah')
    plt.grid(True, alpha=0.3)

    # Simpan grafik
    plot_scatter_path = os.path.join(IMAGE_FOLDER, 'grafik_scatter_as_is.png')
    plt.savefig(plot_scatter_path)
    plt.close()

    # Mengirim data ke template HTML
    return render_template('index.html', stats_table=stats)

if __name__ == '__main__':
    app.run(debug=True)