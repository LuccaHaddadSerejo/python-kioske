from menu import products


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")

    for dict in products:
        if dict["_id"] == id:
            return dict

    return {}


def get_products_by_type(typeParam: str):
    if type(typeParam) != str:
        raise TypeError("product type must be a str")
    new_list = []
    for dict in products:
        if dict["type"] == typeParam:
            new_list.append(dict)

    if len(new_list) == 0:
        return []
    else:
        return new_list


def add_product(menu: list, **kwargs: dict):
    if menu == []:
        kwargs["_id"] = 1
    else:
        id_list = []
        for item in menu:
            id_list.append(item["_id"])
        id_list.sort(reverse=True)
        biggest_id = id_list[0]
        new_id = biggest_id + 1
        kwargs["_id"] = new_id

    menu.append(kwargs)
    return kwargs


def menu_report():
    p_count = len(products)

    v_list = []
    for item in products:
        v_list.append(item["price"])

    sum = 0
    for value in v_list:
        sum += value

    a_price = sum / p_count

    t_list = []
    for item in products:
        t_list.append(item["type"])

    veg_products = t_list.count("vegetable")
    dairies_products = t_list.count("dairy")
    drink_products = t_list.count("drink")
    bakery_products = t_list.count("bakery")
    fruit_products = t_list.count("fruit")

    p_dict = {
        "dairy": dairies_products,
        "drink": drink_products,
        "bakery": bakery_products,
        "fruit": fruit_products,
        "vegetable": veg_products,
    }

    m_c_type = max(p_dict, key=p_dict.get)

    return f"Products Count: {p_count} - Average Price: ${a_price.__round__(2)} - Most Common Type: {m_c_type}"
