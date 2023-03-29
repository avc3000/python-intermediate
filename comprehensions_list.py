### Comprehension List ###
my_original_list = [10, 20, 30, 40, 50]
print(my_original_list)

my_list = [i for i in range(5)]
print(my_list)

my_range = range(8)
print(list(my_range))

my_new_list = [i + 2 for i in range(8)]
print(my_new_list)

my_new_list = [i * i for i in range(8)]
print(my_new_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)
