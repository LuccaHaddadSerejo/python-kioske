from management.product_handler import (
    add_product,
    get_product_by_id,
    get_products_by_type,
    menu_report,
    products,
)

from management.tab_handler import calculate_tab

if __name__ == "__main__":
    get_product_by_id(32)
    get_products_by_type("dairy")
    new_product = {
        "title": "Suco de React",
        "price": 5.0,
        "rating": 4,
        "description": "Suco de React com Limao",
        "type": "drink",
    }
    add_product(products, **new_product)
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    calculate_tab(table_1)
    calculate_tab(table_2)
    menu_report()
    ...
