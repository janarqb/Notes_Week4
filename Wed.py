# 30ые годы были lamda функции, в пайтон включили их в 1994 годах 
# def identity(x):
#     return x + 1 

# lambda x:x  

# lambda x:x +1

# (lambda x:x +1) (2)

# add_one = lambda x: x+1
# add_one(2)

# def fut_to_meters(num_fut):
#     return f'{round(num_fut/3.2000)} meters'
# fut = [10, 15, 5, 6, 7]
# meters = list(map(fut_to_meters, fut))
# print(meters)

# futs = [10, 15, 5, 6, 7]
# meters = list(map(lambda x: round(x/3.2808), futs))
# print(meters)

# data = ['John', 'Steve', 'Angela', 'Arnold']
# filter_data = list(filter(lambda x:x.startswith('A'), data))
# print(filter_data)

# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

# from functools import reduce
# items = [1, 24, 17, 9, 32, 2]
# all_max = reduce(lambda a, b: a if (a>b) else b, items)
# print(all_max)

# from functools import reduce 
# seq = [2, 3, 4, 5, 6]
# multiply = reduce(lambda a, b: a*b, seq)

# print(multiply)

users = [
        {'username': 'Petay', 'comment':['I love icecream']}, 
        {'username': 'Vasya', 'comment':[]},
        {'username': 'Petay', 'comment':['I love icecream']},
        {'username': 'Petay', 'comment':[]},
        {'username': 'Petay', 'comment':['I love icecream']}
        ]
print(list(filter(lambda a:not a ['comment'], users)))



