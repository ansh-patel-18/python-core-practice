# list_a = [1,2]
# list_a.append([3,4])
# print(list_a)

# list_b = [1,2]
# list_b.extend([3,4])
# print(list_b)

number = [15, 22, 78, 18, 100]
taxed_numbers = [n * 1.10 for n in number if n>20]
print(taxed_numbers)