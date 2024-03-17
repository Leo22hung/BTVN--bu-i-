def square(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

numbers = [1, 2, 3, 4, 5]
squared_number = square(numbers)

print(squared_number)