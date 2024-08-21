from time import perf_counter

my_dict={'Sveta':1963,'Vova':1993, 'Kolya':1992}
print(my_dict)
print(my_dict['Sveta'])
my_dict['Tanya']=2001
print(my_dict['Tanya'])
my_dict.update({'Masha':1990,'Sasha':2000})
a=my_dict.pop('Sveta')
print(a)
print(my_dict)

my_set={1,2,2,10,1,'Sveta'}
print(my_set)
my_set.add((50,13))
print(my_set)
print(my_set.discard(3))
print(my_set)