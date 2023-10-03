import csv
import random
with open('books.csv') as f:
    sum = 0
    book = []
    reader = csv.reader(f, delimiter=';')
    books = list(reader)
    print(f'Колличество записей в файле: {len(books) - 1}')
    for row in books:
        if len(row[1])>30:
            sum+=1
    print(f'Колличетсво книг у которых в названии больше 30 симолов: {sum}')
    s = input('Введите имя автора, которого вы хотите найти: ')
    for row in books:
        if s in (row[3] or row[4]) and (('2015' or '2018') in row[6]): #8 вариант
            book.append(row[1])
    print(f'2015 или 2018 года книги автора {s}: {book}')
with open('bibliographic_links.txt', 'w', encoding='UTF-8') as file:
    for i in range(20):
        r = random.randrange(1,len(books)-1)
        file.write(f'{r}, Автор - {books[r][3]}, Книга - {books[r][1]}, дата: {books[r][6]}\n')
