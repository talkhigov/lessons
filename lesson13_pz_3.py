import math

old_list = [1, 4, -6, 9, -9, 25, 16, -81]
result = []

for i in old_list:
    if i > 0:
        result.append(int(math.sqrt(i)))
    elif i < 0:
        result.append(i)

print(old_list)
print(result)

# result = [int(math.sqrt(i)) for i in old_list if i > 0]
# result += [j for j in old_list if j < 0]
# print(result)