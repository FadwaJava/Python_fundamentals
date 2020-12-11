products = ['appel', 'aap', 'aap', 'opa', 'bompa', 5, True, True, False, 'appel', 'opa', 'aap']


def frequency(list_products):
    set_products = set(list_products)
    dict_products = {p: list_products.count(p) for p in set_products}
    print(list_products)
    print(dict_products)


frequency( products )
