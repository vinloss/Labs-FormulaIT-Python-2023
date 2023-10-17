# TODO Найдите количество книг, которое можно разместить на дискете
page_in_book = 100
lines_on_the_page = 50
characters_in_line = 25
bites_in_characters = 4

memory_on_book = page_in_book * lines_on_the_page * characters_in_line * bites_in_characters
memory_available = 1.44 * (1024 * 1024)
result = int(memory_available // memory_on_book)

print("Количество книг, помещающихся на дискету:", result)
