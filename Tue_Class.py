# nums = [5, 2, 8, 9, 5, 1, 2, 4]
# new_list = sorted(nums)
# print(nums)

#hex - 16 система исчесления 


#vars () - дает доступ к переменным 

# old_list = ['1', '2', '3', '4', '5']
# # new_list = []

# # for x in old_list:
# #     new_list.append(int(x))
# # print(new_list)
# def bla_bla(x):
#     x = int(x)
#     return x**x

# # new_list =list(map(int, old_list))
# # print(new_list)

# new_list =list(map(bla_bla, old_list))
# print(new_list)

# def func(x, y, z):
#     return x+y+z

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [3, 4, 5]

# new_list = list(map(func, l1, l2, l3))
# print(new_list)

# def filt(word):
#     if word.startswith('A'):
#         return True

# data = ['Dastan', 'Aybek', 'Janar', 'Vasya', 'Arnold', 'Bruce']
# filtered_data = list(filter(filt, data))
# print(filtered_data)

from functools import reduce 

# def sum (x, y):
#     return x+y
# items = [1, 2, 3, 4]
# sum = reduce(sum, items, 10)
# print(sum)

sentences = ['Капитан джек воробей',
            "Капитан вол",
            'C']
def counter(a, x):
    a = a+x.count('капитан')
    return a

cap_count = reduce(counter, sentences, 0)
print(cap_count)
