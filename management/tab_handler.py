from menu import products


def calculate_tab(tableOrders: list):
    sum = []
    res = 0
    for item in tableOrders:
        for product in products:
            if item["_id"] == product["_id"]:
                calc = item["amount"] * product["price"]
                sum.append(calc)

    for value in sum:
        res += value

    return {"subtotal": f"${res.__round__(2)}"}
