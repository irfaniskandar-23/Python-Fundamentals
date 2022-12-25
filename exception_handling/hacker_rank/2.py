import re


def validate_regex(expression):
    try:
        re.compile(expression)
    except:
        return False
    return True


counter = int(input())
data = {key: input() for key in range(counter)}


for item in data.values():
    result = validate_regex(item)
    print(result)
