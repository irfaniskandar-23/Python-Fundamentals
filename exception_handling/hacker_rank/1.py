
counter = int(input())
data = {key: input().split() for key in range(counter)}

for index, values in enumerate(data.values()):
    try:
        converted_data = [int(item) for item in values]
        dividend, divisor = converted_data[0], converted_data[1]
        result = dividend // divisor

    except ZeroDivisionError as error:
        print(f"Error Code: {error}")

    except ValueError as error:
        print(f"Error Code: {error}")

    else:
        print(result)
