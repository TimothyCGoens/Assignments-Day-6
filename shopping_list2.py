

stores = []


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __repr__(self):
        return(self.name)


class GroceryItem:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return(self.name)


def view_all_stores():
    for store in stores:
        print(f"""
        {stores.index(store) + 1}) {store.name} - {store.items}
        """)

def show_menu():
    print("""
    -------------------------------
    Press 1 to add store.
    Press 2 to add item to a store.
    Press 3 to view all stores.
    Press q to quit.
    -------------------------------
    """)

def add_store():
    name = input("""
    Enter store name:
    """)
    store = Store(name)
    stores.append(store)

def add_item():
    store_choice = int(input("""
    Press the number of the store you wish to shop from:
    """))
    item = input("""
    What would you like to buy and how many do you need?
    (Ex: Pizza 1)
    """)
    for store in stores:
        if store_choice == stores.index(store) + 1:
            store.items.append(GroceryItem(item))



user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("""
    Enter your choice: """)

    if user_input == "1":
        add_store()
    elif user_input == "2":
        add_item()
    elif user_input == "3":
        view_all_stores()
    else:
        print("""
    Thank you and have a great day!
        """)
