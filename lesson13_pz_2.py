numbers = [2, 3, 4, 6, 8, 9, -4, -6, 15, -17, 13, 18, -9]
new_numbers = []
for i in numbers:
    if i > 0 and i % 3 == 0 and i % 4 != 0:
        new_numbers.append(i)

print(new_numbers)

result = [i for i in numbers if i > 0 and i % 3 == 0 and i % 4 != 0]
print(result)