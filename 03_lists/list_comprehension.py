# List Comprehension Practice
# Topic: Transforming and filtering lists


# Challenge 1: Squaring numbers

numbers = [1, 2, 3, 4, 5]

squares = [
    number ** 2
    for number in numbers
]

print("Squares:", squares)


# Challenge 2: Double numbers

numbers = [3, 5, 7, 9]

doubled = [
    number * 2
    for number in numbers
]

print("Doubled:", doubled)


# Challenge 3: Filter even numbers

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print("Even:", even_numbers)


# Challenge 4: Clean names

names = [
    " alice ",
    " BOB",
    "charlie "
]

clean_names = [
    name.strip().title()
    for name in names
]

print("Clean names:", clean_names)
