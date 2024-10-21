my_dict = {'Ruslan': 1995, 'Natalya': 1977, 'Artem': 2004, 'Marina': 2009}
print(my_dict)
print(my_dict['Ruslan'])
print(my_dict.get('Vitaliy'))
my_dict.update({'Oleg': 1993,
                'Andrey': 1994})
deleted_name = my_dict.pop('Artem')
print(deleted_name)
print(my_dict)

my_set = {1, 1, 2, 1, 3, True, 3, 5, 'Ascension', 5}
print(my_set)
my_set.add(4.4), my_set.add((6, 7))
my_set.discard(2)
print(my_set)