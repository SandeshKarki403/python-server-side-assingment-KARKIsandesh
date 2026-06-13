import json
from tabulate import tabulate

data = [
    {"name": "zinc", "price": 255, "quantity": 2},
    {"name": "iron", "price": 150, "quantity": 5},
    {"name": "copper", "price": 300, "quantity": 1}
]

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    main = json.load(f)


for item in main:
    item["total"] = item["price"] * item["quantity"]

print(tabulate(main, headers="keys", tablefmt="grid"))
