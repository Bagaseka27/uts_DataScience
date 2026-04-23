from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

df = pd.read_csv("clean_data_sleep_health.csv")

IMAGE_FOLDER = "static/images"
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

def save_plot(nama_file):
    path = os.path.join(IMAGE_FOLDER, nama_file)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

@app.route('/')
def index():
    desc = df.describe().to_html()

    # 2. Umur
    plt.figure()
    df['Age'].hist()
    plt.title("Distribusi Age")
    plt.xlabel("Age")
    plt.ylabel("Frekuensi")
    plt.grid()
    save_plot("distribusi_umur.png")

    # 3. Gender
    plt.figure()
    df['Gender'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Distribusi Gender")
    plt.ylabel("")
    save_plot("gender.png")

    # 4. Occupation
    plt.figure()
    df['Occupation'].value_counts().plot(kind='bar')
    plt.title("Distribusi Occupation")
    plt.xlabel("Occupation")
    plt.ylabel("Jumlah")
    plt.xticks(rotation=45)
    plt.grid()
    save_plot("occupation.png")

    # 5. Sleep Duration
    plt.figure()
    df['Sleep Duration'].hist()
    plt.title("Distribusi Sleep Duration")
    plt.xlabel("Sleep Duration")
    plt.ylabel("Frekuensi")
    plt.grid()
    save_plot("durasi_tidur.png")

    # 6. Sleep Disorder
    plt.figure()
    df['Sleep Disorder'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Distribusi Sleep Disorder")
    plt.ylabel("")
    save_plot("gangguan_tidur.png")

    # 7. Age vs Sleep Duration
    plt.figure()
    plt.scatter(df['Age'], df['Sleep Duration'])
    plt.title("Age vs Sleep Duration")
    plt.xlabel("Age")
    plt.ylabel("Sleep Duration")
    plt.grid()
    save_plot("umur_vs_tidur.png")

    # 8. Physical Activity Level vs Sleep Duration
    plt.figure()
    plt.scatter(df['Physical Activity Level'], df['Sleep Duration'])
    plt.title("Physical Activity Level vs Sleep Duration")
    plt.xlabel("Physical Activity Level")
    plt.ylabel("Sleep Duration")
    plt.grid()
    save_plot("aktivitas_vs_tidur.png")

    # 9. Stress Level vs Sleep Duration
    plt.figure()
    plt.scatter(df['Stress Level'], df['Sleep Duration'])
    plt.title("Stress Level vs Sleep Duration")
    plt.xlabel("Stress Level")
    plt.ylabel("Sleep Duration")
    plt.grid()
    save_plot("stress_vs_tidur.png")

    # 10. Quality of Sleep vs Sleep Duration
    plt.figure()
    plt.scatter(df['Quality of Sleep'], df['Sleep Duration'])
    plt.title("Quality of Sleep vs Sleep Duration")
    plt.xlabel("Quality of Sleep")
    plt.ylabel("Sleep Duration")
    plt.grid()
    save_plot("kualitas_vs_tidur.png")

    # 11. Age vs Physical Activity Level
    plt.figure()
    plt.scatter(df['Age'], df['Physical Activity Level'])
    plt.title("Age vs Physical Activity Level")
    plt.xlabel("Age")
    plt.ylabel("Physical Activity Level")
    plt.grid()
    save_plot("umur_vs_aktivitas.png")

    return render_template("index.html", desc=desc)

if __name__ == '__main__':
    app.run(debug=True)