class InventoryManagement:
    def __init__(self):
        self.inventory = {}

    def add_item(self):
        name = input("Item name: ").strip().lower()
        if name in self.inventory:
            print("Item already exists.")
            return
        
        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            if price > 0 and quantity > 0:
                self.inventory[name] = {"price": price, "quantity": quantity}
                print(f"Added {name}")
            else:
                print("Price and quantity must be positive.")
        except ValueError:
            print("Invalid input.")

    def remove_item(self):
        name = input("Item to remove: ").strip().lower()
        if name in self.inventory:
            del self.inventory[name]
            print(f"Removed {name}")
        else:
            print("Item not found.")

    def search_item(self):
        search = input("Search for: ").strip().lower()
        found = [item for item in self.inventory if search in item]
        
        if found:
            for item in found:
                details = self.inventory[item]
                print(f"{item}: ${details['price']}, qty: {details['quantity']}")
        else:
            print("No items found.")

    def update_item(self):
        name = input("Item to update: ").strip().lower()
        if name not in self.inventory:
            print("Item not found.")
            return
            
        try:
            price = float(input(f"New price (current: ${self.inventory[name]['price']}): "))
            quantity = int(input(f"New quantity (current: {self.inventory[name]['quantity']}): "))
            if price > 0 and quantity > 0:
                self.inventory[name] = {"price": price, "quantity": quantity}
                print(f"Updated {name}")
            else:
                print("Price and quantity must be positive.")
        except ValueError:
            print("Invalid input.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
            
        for item, details in self.inventory.items():
            print(f"{item}: ${details['price']}, qty: {details['quantity']}")

    def run(self):
        while True:
            print("\n1. Add  2. Remove  3. Search  4. Update  5. Display  6. Exit")
            choice = input("Choose (1-6): ")
            
            if choice == '1': self.add_item()
            elif choice == '2': self.remove_item()
            elif choice == '3': self.search_item()
            elif choice == '4': self.update_item()
            elif choice == '5': self.display_inventory()
            elif choice == '6': break
            else: print("Invalid choice.")

if __name__ == "__main__":
    InventoryManagement().run()