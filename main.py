import csv

stock_data = []
restock_items = []

#Read CSV

try:
    with open("stock.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            stock_data.append(row)

except FileNotFoundError:
    print("stock.csv is not found")
    exit()

#process data

for item in stock_data:

    try:
        name = item["item_name"]
        quantity =  int(item["current_quantity"])
        threshold = int(item["reorder_threshold"])

    except (ValueError, KeyError):
        continue

    if quantity < threshold:

        if quantity <= threshold * 0.25:
            priority = "Critical"
        else:
            priority = "Low"

        reorder = threshold - quantity

        restock_items.append({
            "Item": name,
            "Current": quantity,
            "Threshold": threshold,
            "Priority": priority,
            "Reorder": reorder
        })

#print report

print("=" * 50)
print("RESTOCK REPORT")
print("=" * 50)

if len(restock_items) == 0:
    print("Everything is Fully stocked")
else:
    for item in restock_items:
        print(f"""
item Name     : {item['Item']}
Current Stock : {item['Current']}
Threshold     : {item['Threshold']}
Priority      : {item['Priority']}
Reorder Qty   : {item['Reorder']}

""")

#Simulated email

print("\n")
print("=" * 50)
print("EMAIL ALERT")
print("=" * 50)

print("Subject: Inventory Restock Alert\n")

print("Dear Warehouse Manager\n")

print ("THe following items require restocking:\n")

for item in restock_items:
    print(f" - {item['Item']} ({item['Priority']})")
print("\nRegards")
print("Inventory Automation System")

#Export CSV

with open("restock_report.csv", "w", newline="") as file:

    fields = [
        "Item",
        "Current",
        "Threshold",
        "Priority",
        "Reorder"
    ]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerows(restock_items)

print("\nCSV report generated Successfully")


