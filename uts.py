from flask import Flask, render_template
import pandas as pd
import matplotlib
matplotlib.use('Agg') # WAJIB untuk server seperti PythonAnywhere agar tidak error GUI
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(base_dir, "clean_data_sleep_health.csv")
df = pd.read_csv(csv_path)

IMAGE_FOLDER = os.path.join(base_dir, "static", "images")
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

def save_plot(nama_file):
    path = os.path.join(IMAGE_FOLDER, nama_file)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

@app.route('/')
def index():
    desc = df.describe().to_html(classes='table table-striped')

    # Buat 9 Grafik (Pastikan nama file sesuai dengan yang dipanggil di HTML)
    
    # 1. Age
    plt.figure()
    df['Age'].hist(color='#4c51bf')
    plt.title("Distribusi Umur")
    save_plot("distribusi_umur.png")

    # 2. Gender
    plt.figure()
    df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#4c51bf', '#00b4d8'])
    plt.title("Distribusi Gender")
    save_plot("gender.png")

    # 3. Occupation
    plt.figure()
    df['Occupation'].value_counts().plot(kind='bar', color='#4c51bf')
    plt.title("Distribusi Pekerjaan")
    plt.xticks(rotation=45)
    save_plot("occupation.png")

    # 4. Sleep Duration
    plt.figure()
    df['Sleep Duration'].hist(color='#00b4d8')
    plt.title("Durasi Tidur")
    save_plot("durasi_tidur.png")

    # 5. Sleep Disorder
    plt.figure()
    df['Sleep Disorder'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Gangguan Tidur")
    save_plot("gangguan_tidur.png")

    # 6. Age vs Sleep
    plt.figure()
    plt.scatter(df['Age'], df['Sleep Duration'], color='#4c51bf', alpha=0.5)
    plt.title("Umur vs Durasi Tidur")
    save_plot("umur_vs_tidur.png")

    # 7. Activity vs Sleep
    plt.figure()
    plt.scatter(df['Physical Activity Level'], df['Sleep Duration'], color='#00b4d8')
    plt.title("Aktivitas vs Tidur")
    save_plot("aktivitas_vs_tidur.png")

    # 8. Stress vs Sleep
    plt.figure()
    plt.scatter(df['Stress Level'], df['Sleep Duration'], color='#e53e3e')
    plt.title("Stress vs Tidur")
    save_plot("stress_vs_tidur.png")

    # 9. Quality vs Sleep
    plt.figure()
    plt.scatter(df['Quality of Sleep'], df['Sleep Duration'], color='#38a169')
    plt.title("Kualitas vs Durasi Tidur")
    save_plot("kualitas_vs_tidur.png")

    return render_template("index.html", desc=desc)
