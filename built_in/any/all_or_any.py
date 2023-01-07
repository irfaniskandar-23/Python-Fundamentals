'''
any() -> return TRUE if any(minimum=1) element in iterable satisfy the condition
all() -> return TRUE if all(all required) element in iterable satisfy the condition 
'''


list_size = int(input())
data = [int(number) for number in input().split()][:list_size]
print(all([item >= 0 for item in data]) and any(
    map(lambda x: str(x) == str(x)[::-1], data)))


# num_list = [1, 2, 3, 4]


# # python checl all number in list are positive
# print(all(num >= 0 for num in num_list))
