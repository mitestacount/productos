from crossmodules.connections.database import DatabaseTest


def get_products_by_user_id(user_id: int):
    query = '''
        SELECT products.product_name, products.price
        FROM products
        JOIN user_products ON products.product_id = user_products.product_id
        WHERE user_products.user_id = ?
    '''
    parameters = (user_id,)
    return DatabaseTest.select_data(query, parameters)


if __name__ == '__main__':
    iduser: int = 2
    products = get_products_by_user_id(2)
    print(products)
