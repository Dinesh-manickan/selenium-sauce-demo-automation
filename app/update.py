import os
from utils.data_handler import read_json, save_json
from utils.error_handler import log_error


def update_price():
    path = "data/products.json"

    try:
        if os.path.exists(path):
            data = read_json(path)
            product_titles = list(data.keys())

            if len(product_titles) >= 3:
                third_product_title = product_titles[2]
                data[third_product_title]['price'] = '$100'
                save_json(path, data)
                print(
                    f"Price of the third product '{third_product_title}' has been updated to $100.")
            else:
                log_error("Less than three products found in the JSON file.")
        else:
            log_error(f"File '{path}' not found.")

    except Exception as e:
        log_error(f"An error occurred while updating the price: {e}")


if __name__ == "__main__":
    update_price()
