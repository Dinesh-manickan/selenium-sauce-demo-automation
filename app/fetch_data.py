from utils.api_call_handler import fetch_json_data
from utils.data_handler import save_json
import os


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_json_data(url)

    if data:
        titles = {item['title']: {"id": item['id'],
                                  "title": item['title']} for item in data}

        path = os.path.join("data", "new_demo_title.json")
        save_json(path, titles)
        print("All titles saved successfully in", path)
    else:
        print("Failed to fetch data.")


if __name__ == "__main__":
    fetch_data()
