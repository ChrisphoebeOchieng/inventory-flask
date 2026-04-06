import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    print("\n1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

def view():
    res = requests.get(f"{BASE_URL}/inventory")
    print(res.json())

def add():
    name = input("Name: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))
    barcode = input("Barcode: ")

    res = requests.post(f"{BASE_URL}/inventory", json={
        "product_name": name,
        "price": price,
        "stock": stock,
        "barcode": barcode
    })

    print(res.json())

def update():
    id = input("ID: ")
    res = requests.patch(f"{BASE_URL}/inventory/{id}", json={
        "price": int(input("New price: ")),
        "stock": int(input("New stock: "))
    })
    print(res.json())

def delete():
    id = input("ID: ")
    res = requests.delete(f"{BASE_URL}/inventory/{id}")
    print(res.json())

while True:
    menu()
    choice = input("Choice: ")

    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    else:
        break