import sqlite3
import requests
import time

def setup_db():
    conn = sqlite3.connect("internet.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS sites (url TEXT)' )
    sites = []
    cursor.executemany('INSERT INTO sites VALUES (?)', sites)
    conn.commit()
    conn.close()

setup_db()

def search_in_web(keyword):
    conn = sqlite3.connect("internet.db")
    cursor = conn.cursor()
    cursor.execute('SELECT url FROM sites')
    urls = [row[0] for row in cursor.fetchall()]
    conn.close()

    results = []

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            count = response.text.lower().count(keyword.lower())
            if count > 0:
                results.append({'url': url, 'count': count})
        except Exception as e:
            print(f"Помилка доступу до {url}: {e}")

    sorted_results = sorted(results, key=lambda x: x['count'], reverse=True)
    return sorted_results

def has_sites():
    conn = sqlite3.connect("internet.db")
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM sites')
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def main():
    while True:
        print("----------Меню----------")
        print("1. Пошук інформації")
        print("2. Додати сайт до БД")
        print("3. Очистити БД")
        print("4. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            if not has_sites():
                print("База данних порожня! Спочатку додайте сайт.")
                continue

            key = input("Введіть слово для пошуку: ")
            res = search_in_web(key)
            print("Результати пошуку: ")
            for item in res:
                print(f"{item['url']} - знайдено {item['count']} слів")

        elif choice == "2":
            new_url = input("Введіть URL (з http/https): ")
            conn = sqlite3.connect("internet.db")
            conn.execute('INSERT INTO sites VALUES (?)', (new_url,))
            conn.commit()
            conn.close()
            print("Сайт додано")

        elif choice == "3":
            if not has_sites():
                print("База данних вже порожня!")
                continue

            conn = sqlite3.connect("internet.db")
            conn.execute('DELETE FROM sites')
            conn.commit()
            conn.close()
            print("БД очищено")

        elif choice == "4":
            break

        else:
            print("Виберіть 1 з пунктів (1, 2, 3, 4)")
            print("Перезапуск через 5 секунд")
            print("---------------------------------")
            time.sleep(5)
            main()

if __name__ == "__main__":
    main()