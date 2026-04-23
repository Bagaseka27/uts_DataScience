from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

FOLDER_GAMBAR = os.path.join('static', 'images')
if not os.path.exists(FOLDER_GAMBAR):
    os.makedirs(FOLDER_GAMBAR)

@app.route('/')
def index():
    df = pd.read_csv('clean_data_sleep_health.csv')

    judul = 'Visualisasi Data Sleep Health'

    # 1. Histogram Durasi Tidur
    plt.figure()
    plt.hist(df['Sleep Duration'].dropna(), bins=10)
    plt.title(judul)
    plt.xlabel('Durasi Tidur (Jam)')
    plt.ylabel('Frekuensi')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'histogram_durasi_tidur.png'))
    plt.close()

    # 2. Diagram Batang Gender
    plt.figure()
    df['Gender'].value_counts().plot(kind='bar')
    plt.title(judul)
    plt.xlabel('Gender')
    plt.ylabel('Jumlah')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_batang_gender.png'))
    plt.close()

    # 3. Diagram Garis Usia
    plt.figure()
    df.groupby('Age')['Sleep Duration'].mean().plot(kind='line', marker='o')
    plt.title(judul)
    plt.xlabel('Usia')
    plt.ylabel('Rata-rata Durasi Tidur (Jam)')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_garis_usia.png'))
    plt.close()

    # 4. Scatter Tidur vs Kualitas
    plt.figure()
    plt.scatter(df['Sleep Duration'], df['Quality of Sleep'])
    plt.title(judul)
    plt.xlabel('Durasi Tidur (Jam)')
    plt.ylabel('Kualitas Tidur')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_titik_tidur.png'))
    plt.close()

    # 5. Pie Chart Gender
    plt.figure()
    df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(judul)
    plt.ylabel('')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_lingkaran_gender.png'))
    plt.close()

    # 6. Histogram Kualitas Tidur
    plt.figure()
    plt.hist(df['Quality of Sleep'].dropna(), bins=10)
    plt.title(judul)
    plt.xlabel('Kualitas Tidur')
    plt.ylabel('Frekuensi')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'histogram_kualitas_tidur.png'))
    plt.close()

    # 7. Diagram Batang Gangguan Tidur
    plt.figure()
    df['Sleep Disorder'].value_counts().plot(kind='bar')
    plt.title(judul)
    plt.xlabel('Jenis Gangguan')
    plt.ylabel('Jumlah')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_batang_gangguan_tidur.png'))
    plt.close()

    # 8. Diagram Batang Pekerjaan
    plt.figure()
    df['Occupation'].value_counts().head(10).plot(kind='bar')
    plt.title(judul)
    plt.xlabel('Pekerjaan')
    plt.ylabel('Jumlah')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_batang_pekerjaan.png'))
    plt.close()

    # 9. Scatter Aktivitas vs Tidur
    plt.figure()
    plt.scatter(df['Physical Activity Level'], df['Sleep Duration'])
    plt.title(judul)
    plt.xlabel('Aktivitas Fisik')
    plt.ylabel('Durasi Tidur (Jam)')
    plt.savefig(os.path.join(FOLDER_GAMBAR, 'diagram_titik_aktivitas.png'))
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)