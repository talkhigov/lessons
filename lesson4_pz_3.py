numbers = [2, 2, 5, 12, 8, 12, 3, 3, 3, 1, 4, 4, 4, 4, 6]
result = []
for i in numbers:
    if not numbers.count(i) > 1:
        result.append(i)
print(result)

result = [i for i in numbers if not numbers.count(i) > 1]
print(result)