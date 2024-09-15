# 1. Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.


# arr_one: list[str] = []
# arr_two: list[str] = []
#
# with open('task-1-text-one.txt', encoding='utf-8') as f1:
#     arr_one = f1.read().split(', ')
#
# with open('task-1-text-two.txt', encoding='utf-8') as f2:
#     arr_two = f2.read().split(', ')
#
# for word_one in arr_one:
#     if word_one not in arr_two:
#         print(word_one)
#
# for word_two in arr_two:
#     if word_two not in arr_one:
#         print(word_two)


# 2. Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по
# исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.


# arr_text: list[str] = []
# count_symbol: int = 0
# count_lines: int = 0
#
# count_vowel: int = 0
# count_consonant: int = 0
# count_num: int = 0
#
# arr_vowel: list[str] = ['А', 'Ё', 'У', 'Ы', 'Е', 'О', 'Э', 'Я', 'И', 'Ю']
# arr_consonant: list[str] = ['Й', 'Ц', 'К', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф',
#                             'В', 'П', 'Р', 'Л', 'Д', 'Ж', 'Ч', 'С', 'М' 'Т', 'Ь', 'Б']
# arr_num: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# with open('task-1-text-one.txt', 'r', encoding='utf -8') as f:
#     arr_text = f.read()
# count_symbol = len(arr_text)
#
# with open('task-1-text-one.txt', 'r', encoding='utf -8') as f:
#     count_lines = len(f.readlines())
#
# # with open('task-1-text-one.txt', 'r', encoding='utf -8') as f:
#
# arr_text = list(map(str.upper, arr_text))
#
# for vowel_letter in arr_text:
#     if vowel_letter in arr_vowel:
#         count_vowel += 1
#
# for consonant_letter in arr_text:
#     if consonant_letter in arr_consonant:
#         count_consonant += 1
#
# for num in arr_text:
#     if num in arr_num:
#         count_num += 1
#
# with open('task-2-result', 'w', encoding='utf-8') as f:
#     f.write('■ Количество символов: ' + str(count_symbol) + '\n')
#     f.write('■ Количество строк: ' + str(count_lines) + '\n')
#     f.write('■ Количество гласных букв: ' + str(count_vowel) + '\n')
#     f.write('■ Количество согласных букв: ' + str(count_consonant) + '\n')
#     f.write('■ Количество цифр: ' + str(count_num))


# 3. Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.


# lines = None
# lines_result = None
# text_result = None
#
# with open('task-3-text.txt', encoding='utf-8') as f:
#     lines = f.readlines()
#     lines_result = lines[:-1]
#     text_result = ','.join(lines_result)
#
# with open('task-3-result', 'w', encoding='utf-8') as f:
#     f.write(text_result)


# 4. Дан текстовый файл. Найти длину самой длинной строки.

# max_length = 0
# with open('task-4-text.txt', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         length = len(line) - 1
#         if length > max_length:
#             max_length = length
# print('Длинна самой длинной строки равна: ', max_length)


# 5. Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.

# word: str = 'Привет'
#
# with open('task-5-text.txt', encoding='utf-8') as f:
#     words = f.read().split()
#     print(words.count(word))