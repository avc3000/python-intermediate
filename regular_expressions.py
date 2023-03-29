### Regular Expressions ###
import re

my_string = "Example for regular expressions, 1 good example"
my_other_string = "My name is Antony"

match = re.match("Example", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

print(re.match("This is a lesson", my_other_string))
print(re.match("Regular Expressions", my_string))

# Search
search = re.search("regular", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# FindAll
findall = re.findall("Example", my_string, re.I)
print(findall)

# Split
print(re.split(",", my_string))

# Sub
print(re.sub("example|Example", "EXAMPLE", my_string))
print(re.sub("Example", "RegEx", my_string))

# Patterns
pattern = r"[eE]xample"
print(re.findall(pattern, my_string))

pattern = r"[eE]xample|good"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[1].*"
print(re.findall(pattern, my_string))

# Valid email address
email = "antony@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "antony@gmail.es"
print(re.findall(pattern, email))
