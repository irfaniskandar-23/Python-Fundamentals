'''
any() -> return TRUE if any element in iterable satisfy the condition
all() -> return TRUE if all element in iterable satisfy the condition 
'''


list_size = int(input())
data = [int(number) for number in input().split()][:list_size]
print(all([item >= 0 for item in data]) and any(
    map(lambda x: str(x) == str(x)[::-1], data)))
