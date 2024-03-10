tuple_list = (['HTML', 15, 'M0111'], ['JavaScript', 10, 'M031'], ['Bootstrap', 5, 'M02111'])
sorted_list = sorted(tuple_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))
print(sorted_list)