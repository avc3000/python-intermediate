### Higher Order Functions ###
from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_add_value(1, 2, sum_one))
print(sum_two_values_add_value(1, 3, sum_five))

### Closures ###


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(6))

### Built-in Higher Order Functions ###
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Map


def multiply_two(number):
    return number*2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first, second):
    return first + second


print(reduce(sum_two_values, numbers))