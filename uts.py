from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

app = Flask(__name__)

df = pd.read_csv("clean_data_sleep_health.csv")
df.columns = df.columns.str.strip()

IMAGE_FOLDER = "static/images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def save_plot(nama):
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_FOLDER, nama))
    plt.close()

@app.route('/')
def index():

    # ===== DATA =====
    head = df.head(10).to_html(classes="table", index=False)
    tail = df.tail(10).to_html(classes="table", index=False)
    desc = df.describe().to_html(classes="table")

    # ===== VISUAL =====

    # 1. Gender (Pie)
    plt.figure()
    df['Gender'].value_counts().plot.pie(
        autopct='%1.1f%%',
        colors=['#4F46E5', '#06B6D4']
    )
    plt.title("Distribusi Gender")
    plt.ylabel("")
    save_plot("gender.png")

    # 2. Sleep Duration (Histogram)
    plt.figure()
    plt.hist(df['Sleep Duration'], bins=10, color='#3B82F6')
    plt.title("Distribusi Sleep Duration")
    plt.xlabel("Sleep Duration")
    plt.ylabel("Frekuensi")
    save_plot("sleep_duration.png")

    # 3. 3D Scatter
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(
        df['Sleep Duration'],
        df['Stress Level'],
        df['Quality of Sleep'],
        c=df['Quality of Sleep'],
        cmap='viridis'
    )
    ax.set_xlabel("Sleep Duration")
    ax.set_ylabel("Stress Level")
    ax.set_zlabel("Quality of Sleep")
    plt.title("3D: Sleep Duration vs Stress vs Quality")
    save_plot("3d_tidur.png")

    # 4. Stress vs Sleep Duration (Scatter)
    plt.figure()
    plt.scatter(
        df['Stress Level'],
        df['Sleep Duration'],
        color='#EF4444'
    )
    plt.title("Stress Level vs Sleep Duration")
    plt.xlabel("Stress Level")
    plt.ylabel("Sleep Duration")
    save_plot("stress_vs_tidur.png")

    # 5. Physical Activity vs Sleep Duration (Line)
    plt.figure()
    sorted_df = df.sort_values(by='Physical Activity Level')
    plt.plot(
        sorted_df['Physical Activity Level'],
        sorted_df['Sleep Duration'],
        color='#10B981',
        marker='o'
    )
    plt.title("Physical Activity vs Sleep Duration")
    plt.xlabel("Physical Activity Level")
    plt.ylabel("Sleep Duration")
    save_plot("aktivitas_vs_tidur.png")

    # 6. Physical Activity vs Quality (Scatter)
    plt.figure()
    plt.scatter(
        df['Physical Activity Level'],
        df['Quality of Sleep'],
        color='#8B5CF6'
    )
    plt.title("Physical Activity vs Quality of Sleep")
    plt.xlabel("Physical Activity Level")
    plt.ylabel("Quality of Sleep")
    save_plot("aktivitas_vs_kualitas.png")

    # 7. Quality vs Sleep Duration (Line)
    plt.figure()
    sorted_df2 = df.sort_values(by='Quality of Sleep')
    plt.plot(
        sorted_df2['Quality of Sleep'],
        sorted_df2['Sleep Duration'],
        color='#F59E0B',
        marker='o'
    )
    plt.title("Quality of Sleep vs Sleep Duration")
    plt.xlabel("Quality of Sleep")
    plt.ylabel("Sleep Duration")
    save_plot("kualitas_vs_tidur.png")

    return render_template(
        "index.html",
        head=head,
        tail=tail,
        desc=desc
    )

if __name__ == '__main__':
    app.run(debug=True)