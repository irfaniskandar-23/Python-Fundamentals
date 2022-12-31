'''
# {{28/12/2022:{item_A: 20.00, item_B=10.00}}}
'''
import pandas as pd
import numpy as np
from tabulate import tabulate


def calculate_daily_sale(data):
    daily_sale_dict = dict()

    for line in data:
        date, item, quantity, price = line.split()
        date_key = daily_sale_dict.get(date, None)

        if date_key is not None:
            if item in daily_sale_dict:
                daily_sale_dict[date][item] += float(price) * int(quantity)
            else:
                daily_sale_dict[date][item] = float(price) * int(quantity)
        else:
            daily_sale_dict[date] = {item: float(price) * int(quantity)}

    return daily_sale_dict


def get_total_sale(daily_sale):
    sale_item_A = sale_item_B = sale_item_C = sale_item_D = 0
    for items in daily_sale.values():
        if 'Item_A' in items:
            sale_item_A += items['Item_A']

        if 'Item_B' in items:
            sale_item_B += items['Item_B']

        if 'Item_C' in items:
            sale_item_C += items['Item_C']

        if 'Item_D' in items:
            sale_item_D += items['Item_D']

    item_sale_dict = {
        'Item_A': sale_item_A,
        'Item_B': sale_item_B,
        'Item_C': sale_item_C,
        "item_D": sale_item_D
    }

    return item_sale_dict


if __name__ == '__main__':
    try:
        with open('input.txt') as file:
            data = [line.strip() for line in file]

        daily_sale = calculate_daily_sale(data)
        print(daily_sale['2020-09-25'])
        print(daily_sale['2020-09-25']['Item_B'])

        total_sales = get_total_sale(daily_sale)
        print(total_sales)

    except Exception as error:
        print(f'Error: {error}')
    finally:
        file.close()

    daily_sale_frame = pd.DataFrame.from_dict(daily_sale, orient='index', columns=[
                                              'Item_A', 'Item_B', 'Item_C', 'Item_D'])

    daily_sale_frame = daily_sale_frame.replace(np.nan, 0.0)
    print(tabulate(daily_sale_frame, headers='keys', tablefmt='psql'))
