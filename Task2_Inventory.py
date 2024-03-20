def sort_products(products, sort_key, ascending=True):

    try:
        sorted_products = sorted(products, key=lambda item: item[sort_key])
        if not ascending:
            sorted_products.reverse()
        print(sorted_products)

    except KeyError:
        print("Key not found in dictionary")


if __name__ == "__main__":

    products = [
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product C", "price": 50, "stock": 10},
        {"name": "Product B", "price": 200, "stock": 3},
    ]

    sort_key = "namfe"
    ascending = True

    sorted_products = sort_products(products, sort_key, ascending)
    print(sorted_products)
