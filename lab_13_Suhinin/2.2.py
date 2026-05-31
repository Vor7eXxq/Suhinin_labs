from collections import defaultdict
products = [
    {"name": "iPhone", "category": "Електроніка"},
    {"name": "Банан", "category": "Продукти"},
    {"name": "Ноутбук", "category": "Електроніка"},
    {"name": "Хліб", "category": "Продукти"}
]
grouped_products = defaultdict(list)
for product in products:
    grouped_products[product["category"]].append(product["name"])
print(grouped_products)