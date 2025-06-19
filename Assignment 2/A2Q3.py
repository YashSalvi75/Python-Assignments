def item_prices():
    items = (("Milk", 25), ("Eggs", 50), ("Bread", 20))
    for item in items:
        print(f"{item[0]}: ₹{item[1]}")

item_prices()
