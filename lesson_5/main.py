from files import CSV_FILE, JSON_FILE
import json
from csv import DictReader

# books = []

with open(CSV_FILE, newline='', mode='r') as f:  # открываем на чтение файл csv
    reader = DictReader(f)

    # вариант через list comprehension
    books = [{
        "title": row["Title"],
        "author": row["Author"],
        "pages": int(row["Pages"]),
        "genre": row["Genre"]
    } for row in reader]

    # for row in reader:  # собираем данные по нужным заголовкам
    #     headers = {
    #         "title": row["Title"],
    #         "author": row["Author"],
    #         "pages": int(row["Pages"]),
    #         "genre": row["Genre"]
    #     }
    # books.append(headers)


# users = []

with open(JSON_FILE, mode='r') as f:  # открываем на чтение файл json
    data = json.load(f)

    # ключи, которые нам нужны
    target_keys = ["name", "gender", "address", "age"]

    # вариант через list comprehension
    users = [{key: user[key] for key in target_keys if key in user}
             for user in data]

    # for item in data:
    #     filtered_json = {key: item[key]
    #                      for key in target_keys if key in item}  # итерируемся по дате с пользователями, собираем только нужные ключи
    #     users.append(filtered_json)

total_books = len(books)
total_users = len(users)

# Количество книг на каждого пользователя
books_per_user = total_books // total_users
remaining_books = total_books % total_users  # Оставшиеся книги

book_index = 0  # Индекс текущей книги

for user in users:
    user['books'] = books[book_index:book_index +
                          books_per_user]  # Назначаем книги пользователю

    book_index += books_per_user

    if remaining_books > 0:
        # Добавляем оставшуюся книгу пользователю
        user['books'].append(books[book_index])
        book_index += 1
        remaining_books -= 1

# Сохраняем результат в файл
with open('result.json', 'w') as f:
    json.dump(users, f, indent=4)

print("DONE")
