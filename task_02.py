import csv
import timeit
from BTrees._OOBTree import OOBTree

def load_items_from_csv(file_path):
    items = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = {
                'ID': int(row['ID']),
                'Name': row['Name'],
                'Category': row['Category'],
                'Price': float(row['Price'])
            }
            items.append(item)
    return items

def add_item_to_tree(tree, item):
    tree.insert(item['ID'], {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    })

def add_item_to_dict(items_dict, item):
    items_dict[item['ID']] = {
        'Name': item['Name'],
        'Category': item['Category'],
        'Price': item['Price']
    }

def range_query_tree(tree, min_price, max_price):
    return [item for key, item in tree.items(min_price, max_price) if min_price <= item['Price'] <= max_price]

def range_query_dict(items_dict, min_price, max_price):
    return [item for item in items_dict.values() if min_price <= item['Price'] <= max_price]

def test_performance(file_path, num_queries=100):

    items = load_items_from_csv(file_path)

    tree = OOBTree()
    items_dict = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(items_dict, item)

    def time_query_tree():
        for _ in range(num_queries):
            range_query_tree(tree, 10.0, 50.0)

    def time_query_dict():
        for _ in range(num_queries):
            range_query_dict(items_dict, 10.0, 50.0)

    time_tree = timeit.timeit(time_query_tree, number=1)
    time_dict = timeit.timeit(time_query_dict, number=1)

    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")

file_path = 'generated_items_data.csv'
test_performance(file_path)
