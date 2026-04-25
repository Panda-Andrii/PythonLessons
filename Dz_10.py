import requests
import sqlite3
import time
from datetime import datetime


LAT = 48.45
LON = 34.98


def init_db():
    conn = sqlite3.connect("weather.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT,
        temperature REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_data(temp):
    conn = sqlite3.connect("weather.db")
    cur = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
    INSERT INTO weather (datetime, temperature)
    VALUES (?, ?)
    """, (now, temp))

    conn.commit()
    conn.close()


def get_temperature():
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LAT}&longitude={LON}&current=temperature_2m"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Помилка заходу на сайт")

    data = response.json()

    temp = data["current"]["temperature_2m"]
    return temp

def main():
    init_db()
    print("Запуск збору погоди...")

    while True:
        try:
            temp = get_temperature()
            insert_data(temp)

            print(f"{datetime.now()} | {temp}°C (збережено)")

        except Exception as e:
            print("Помилка:", e)

        time.sleep(1800)


if __name__ == "__main__":
    main()