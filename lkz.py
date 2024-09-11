#Вам следует написать функцию, которая будет получать положительное целое число и возвращать: "Fizz" если число делится на 3 (3, 6, 9 ...), в противном случае преобразуйте данное число в строку (2 -> "2").
# def checkio(num: int) -> str:
#     # your code here
#     return 'Fizz' if num % 3 == 0 else str(num)



# Дана строка и нужно найти ее первое слово.
#
# Строка состоит только из английских символов и пробелов.
# В начале и в конце строки пробелов нет.
#
# def first_word(text: str) -> str:
#     # your code here
#     return text.split()[0]
# print("Example:")
# print(first_word("Hello world"))
# print(first_word("greeting from CheckiO Planet"))


# Вам дано положительное целое число. Определите сколько цифр оно имеет.

# def checkio(number: int) -> int:
#     # your code here
#     return len(str(number))


# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
#
# Вы должны написать функцию, которая принимает положительное целое число и возвращает:
# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5;
# Число, как строку для остальных случаев.

# Taken from mission Just Fizz!

# def checkio(num: int) -> str:
#     # your code here
#     return "Fizz Buzz" if num % 3 == 0 and num % 5 == 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else str(num)
#
#
# print("Example:")
# print(checkio(15))

#Вычислите сумму целых чисел от 1 до заданного N (включая).
# def sum_upto_n(N: int) -> int:
#     # your code here
#     return sum(range(1, N + 1))
#
# print("Example:")
# print(sum_upto_n(11))


#Ваша функция должна принимать строку в качестве входных данных и преобразовывать все первые буквы слов в строке в верхний регистр,
#  превращая строку в регистр заголовка (остальные буквы должны быть в нижнем регистре).
# def to_title_case(sentence: str) -> str:
#     # your code here
#     return ' '.join(word.title() for word in sentence.split(' '))
# print(to_title_case("hello world"))

# def sum_numbers(n):
#
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + sum_numbers(n - 1)
# b = sum_numbers(11)
# print(b)

# list = [[1,2],[3,4]]
# print(sum(list,[]))
#
# print('ab, cd, ef'.title())
#
# def a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return a(n - 1) + a(n - 2)
# for i in range(0,4):
#     print(a(i),end=" ")



# string = "my name is x"
# for i in string.split():
#     print(i, end=", ")


#Эта функция должна принимать неотрицательное целое число в качестве входных данных и возвращать факториал этого числа. Факториал неотрицательного целого числа n является произведением всех положительных целых чисел, меньших или равных n .

# def factorial(n: int) -> int:
#     # your code here
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))


# Вам дается строка и два маркера (начальный и конечный).
# Вы должны найти подстроку, заключенную между этими двумя маркерами. Но есть несколько важных условий.
#
# Начальный и конечный маркеры всегда разные.
# Начальный и конечный маркеры всегда имеют размер 1 символа.
# Начальный и конечный маркеры всегда существуют в строке и следуют один за другим.


def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    return text[text.index(start)+1:text.index(end)]


print(between_markers("What is >apple<", ">", "<"))