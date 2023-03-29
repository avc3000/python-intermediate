### Package Manager ###
from my_package import arithmetics
import requests
import pandas
import numpy

print(numpy.version.version)

numpy_array = numpy.array([1, 2, 3, 4, 5])
print(type(numpy_array))
print(numpy_array * 2)

# pip list
# pip install
# pip uninstall pandas
# pip show numpy

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
print(response)
print(response.status_code)
print(response.json())

# Arithmetic package
print(arithmetics.sum_two_values(1, 4))
