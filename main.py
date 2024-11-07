# text = "Hello World"
#
# print(text[::-1])
# print(text[:-5])
# print(text[6:])

# 1

# number = [1, 2, 3, 4, 5, -1, -2, -3]
#
# musbat = []
# def function():
#     for i in number:
#         if i < 0:
#             musbat.append(i)
#     return musbat
#
# print(function())

# 2


#
# def max_number(number: list) -> int:
#     i = number[0]
#     if len(number) > 1:
#         for num in number:
#             if i < num:
#                 i = num
#         return i
#
#
# number = [1, 2, 3, 4, 5, -1, -2, -3]
# print(max_number(number))

# Vazifa______________________________________________

# 1

# toq = []
# juft = []
# for i in range(1, 11):
#     if i % 2 != 0:
#         toq.append(i)
#     else:
#         juft.append(i)
# print(toq)
# print(juft)

# 2

# number = [1, 2, 3, 4, 5]
#
# sum = 0
# i = 1
# while i < len(number):
#     sum += number[i]
#     i += 1
#
# print(sum)

# 4

# def max_number(number: list) -> int:
#     i = number[0]
#     if len(number) > 1:
#         for num in number:
#             if i < num:
#                 i = num
#         return i
#
#
# number = [1, 2, 3, 4, 5, -1, -2, -3]
# print(max_number(number))

# def min_number(number: list) -> int:
#     i = number[0]
#     if len(number) > 1:
#         for num in number:
#             if i > num:
#                 i = num
#         return i
#
# number = [1,2, 3, 4, 5]
# print(min_number(number))

# 5

# def add_number():
#     number = [1, 2, 3, 4, 5]
#     user = int(input("index kirting: "))
#
#     if user in number:
#         print('bunday qiymat bizda bor')
#     else:
#         number.append(user)
#     return number
#
# print(add_number())

# 6

# def unikal_number(number):
#     i = 0
#     unikal = []
#     for num in number:
#         i += num
#         if num != i:
#             unikal.append(num)
#
#     return unikal
#
# number = [1, 1, 2, 3, 4, 5]
#
# print(unikal_number(number))

# 7

# def reverse_function(text):
#     reverse = []
#     for i in text:
#         reversed_word = ''
#         for char in i:
#             reversed_word = char + reversed_word
#         reverse.append(reversed_word)
#
#     return reverse
#
# text = ["toxir", "abror", "fozil"]
#
# print(reverse_function(text))

# 8
#
# text = "salom dunyo yayayayayayay"
# words = text.split()
# s = ''
# for i in words:
#     if len(i) > len(s):
#         s = i
#
# print(s)

# 9

# def upper_letter(text):
#     s = []
#     for i in text:
#         s.append(i.upper())
#     return s
# text = ["ali", "vali"]
# print(upper_letter(text))

# 10

# def capital_words(text: str):
#     words = text.split()
#     s = []
#     for i in words:
#         if i[0] == i[0].capitalize():
#             s.append(i)
#     return s
#
# text = "Salom dunyo"
# print(capital_words(text))

# 11

# words = "salom yaxshimisiz ishlaringiz yaxshimi"
# word = words.split()
# for i in word:
#     print(len(i))

# 12

# words = "salom yaxshimisiz ishlaringiz yaxshimi"
#
# word = words.split()
# user = input("Qidirayotgan sozingizni kiriting: ")
# found = False
# for i in word:
#     if user == i:
#         print(f"Qidirgan sozingiz mavjud: {user}")
#         found = True
#         break
# if not found:
#     print("siz qidirgan soz yoq")

# 13

# def lower_letter(text):
#     s = []
#     for i in text:
#         s.append(i.lower())
#     return s
# text = ["Ali", "Vali"]
# print(lower_letter(text))

# 14

# file = ["salom", "ali", "vali"]
# user = input("ochirmoqchi bolgan sozingizni kriting: ")
# try:
#     file.remove(user)
#     print(file)
# except Exception:
#     print("unday soz yoq")

# 15
#
# file = ["salom", "ali", "vali"]
# user = input("ochirmoqchi bolgan sozingizni kriting: ")
# try:
#     index = file.index(user)
#     print(index)
# except Exception:
#     print("siz qidirgan sozning indexsi yoq")








