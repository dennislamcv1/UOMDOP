import csv

## Read the quantities and prices from the CSV files
def read_two_column_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        data = {}
        for item, value in reader:
            data[item] = value
    return data

quantities = read_two_column_csv("data/quantities.csv")
prices = read_two_column_csv("data/prices.csv")

## Combine into an inventory dictionary
def create_combined_inventory(quantities, prices):
    combined_data = {}
    for item in quantities:
        combined_data[item] = {
            "quantity": int(quantities[item])
        }
    for item in prices:
        price = float(prices[item].replace("$", ""))
        if item in combined_data:
            combined_data[item]["price"] = price
        else:
            combined_data[item] = {
                "price": price
            }
    return combined_data
inventory = create_combined_inventory(quantities, prices)

## Process a shopping request
def check_one_product(inventory, product, request_qty):
    message = ""

    available_qty = inventory[product]["quantity"]
    price = inventory[product]["price"]

    if request_qty > available_qty:
        qty = available_qty
        apology = f"Sorry, we only have "
    else:
        qty = request_qty
        apology = ""
    
    inventory[product]["quantity"] -= qty
    subtotal = qty * price
    message = (
        f"${qty * price:.2f}: {apology}"
        f"{qty} {"unit" if qty == 1 else "units"} of {product}; "
        f"${price:.2f} per unit.\n"
    )

    return subtotal, message

def process_shopping_request(shopping_request, inventory):
    response = ""
    total = 0
    for product, request_qty in shopping_request.items():
        subtotal, message = check_one_product(inventory, product, request_qty)
        total += subtotal
        response += message
    response += f"----\n${total:.2f} Total\n"
    return response

print(process_shopping_request({"apples": 500, "bananas": 3, "pears": 1}, inventory))