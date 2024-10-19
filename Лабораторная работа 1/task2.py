# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
pages_in_book = 100
lines = 50
symbols = 25
bytes_for_symbol = 4

bytes_for_book = bytes_for_symbol * symbols * lines * pages_in_book
volume_bytes = volume * 1024 * 1024
books = round(volume_bytes//bytes_for_book)

print("Количество книг, помещающихся на дискету:", books)
