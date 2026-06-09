import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# -------------------------
# CREATE (POST)
# -------------------------
def create_order():
    data = {
        "title": "Тестовый заказ",
        "body": "Доставка пиццы",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=data)

    print("\n[CREATE]")
    print("Status:", response.status_code)
    print("Response:", response.json())

    return response.json()


# -------------------------
# READ (GET)
# -------------------------
def get_order(order_id):
    response = requests.get(f"{BASE_URL}/posts/{order_id}")

    print("\n[GET]")
    print("Status:", response.status_code)
    print("Response:", response.json())


# -------------------------
# UPDATE (PUT)
# -------------------------
def update_order(order_id):
    data = {
        "title": "Обновлённый заказ",
        "body": "Обновлённая доставка",
        "userId": 1
    }

    response = requests.put(f"{BASE_URL}/posts/{order_id}", json=data)

    print("\n[UPDATE]")
    print("Status:", response.status_code)
    print("Response:", response.json())


# -------------------------
# DELETE
# -------------------------
def delete_order(order_id):
    response = requests.delete(f"{BASE_URL}/posts/{order_id}")

    print("\n[DELETE]")
    print("Status:", response.status_code)
    print("Response:", response.text)


# -------------------------
# RUN ALL TESTS
# -------------------------
if __name__ == "__main__":
    print("=== SMARTDELIVERY API TESTS ===")

    created = create_order()
    order_id = created.get("id", 1)

    get_order(order_id)
    update_order(order_id)
    delete_order(order_id)

    print("\n=== TESTS COMPLETED ===")