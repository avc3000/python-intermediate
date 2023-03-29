### Challenges ###
"""
THE FAMOUS "FIZZ BUZZ"
Write a program that displays by console the numbers from 1 to 100
substituting the following:
  - Multiples of 3 by the word "fizz"
  - Multiples of 5 by the word "buzz"
  - Multiples of 3 and 5 at the time for the word "fizz buzz"
"""


def fizz_buzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizz buzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizz_buzz()

"""
IT IS "ANAGRAM"?
Write a function that receives two words and returns true or false
depending on whether they are anagrams or not:
  - An anagram consists of forming a word by rearranging all the letters of another initial word
  - It is not necessary to prove that both words exist
  - Two words exactly alike are not anagrams
"""


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))

"""
FIBONACCI
Write a function of the series of 50 numbers starting at 0:
  - The series is composed by a succession of numbers which the next one is always
    the sum of the two previous ones.
"""


def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 51):
        print(prev)

        fib = prev + next
        prev = next
        next = fib


fibonacci()


def is_fibonacci(number):
    n1, n2 = 0, 1
    count = 0
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


is_fibonacci(51)

"""
PRIME NUMBER
Write a function to check a number is prime or not:
  - Prints numbers from 1 to 100.
"""


def prime():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


prime()


def is_prime():
    for i in range(2, 51):
        if (i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and (i % 7 != 0 or i == 7):
            print(i)


is_prime()

"""
REVERSE A STRING
Write a function that reverses the order of a text string without using language-specific functions:
  - Print "dlrow olleH" from "Hello world".
"""


def reverse(text):
    text_len = len(text) - 1
    reversed_text = ""

    for index in range(0, len(text)):
        reversed_text += text[text_len - index]

    return reversed_text


print(reverse("Hello world"))
