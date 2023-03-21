my_list_1 = [2, 5, 8, 2, 12, 12, 4, 7, 1, 1]
my_list_2 = [2, 7, 12, 3]
result = []

for i in my_list_1:
    if i not in my_list_2:
        result.append(i)

result = [i for i in my_list_1 if i not in my_list_2]
print(result)