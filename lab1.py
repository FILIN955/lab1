import csv
import random
with open('books.csv') as f:
    sum = 0
    max_name = 30
    filtered_book = []
    reader = csv.reader(f, delimiter=';')
    books = list(reader)
    print(f'Колличество записей в файле: {len(books) - 1}')
    for book in books:
        book_name = book[1]
        if len(book_name) > max_name:
            sum+=1
    print(f'Колличетсво книг у которых в названии больше 30 симолов: {sum}')
    s = input('Введите имя автора, которого вы хотите найти: ')
    for book in books:
        title = book[1]
        author = book[3]
        full_author = book[4]
        date = book[6]
        if ((s in author) or (s in full_author)) and (('2015' in date) or ('2018' in date)): #8 вариант
            filtered_book.append(title)
    print(f'2015 или 2018 года книги автора {s}: {filtered_book}')
with open('bibliographic_links.txt', 'w', encoding='UTF-8') as file:
    for i in range(20):
        r = random.randrange(1, len(books)-1)
        random_book = books[r]
        author = random_book[3]
        title = random_book[1]
        date = random_book[6]
        file.write(f'{r}, Автор - {author}, Книга - {title}, дата: {date}\n')
