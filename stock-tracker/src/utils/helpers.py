import json
import os

class Tracker:
    def __init__(self, filename='tracker_data.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Load data from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """Save data to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_item(self, category, item):
        """Add an item to a specific category."""
        if category not in self.data:
            self.data[category] = []
        self.data[category].append(item)
        self.save_data()

    def remove_item(self, category, item):
        """Remove an item from a specific category."""
        if category in self.data and item in self.data[category]:
            self.data[category].remove(item)
            self.save_data()

    def view_items(self, category):
        """View all items in a specific category."""
        return self.data.get(category, [])

    def view_all(self):
        """View all categories and their items."""
        return self.data

def main():
    tracker = Tracker()

    while True:
        print("\nTracker Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Items in Category")
        print("4. View All Items")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            item = input("Enter item: ")
            tracker.add_item(category, item)
            print(f"Added '{item}' to '{category}'.")

        elif choice == '2':
            category = input("Enter category: ")
            item = input("Enter item: ")
            tracker.remove_item(category, item)
            print(f"Removed '{item}' from '{category}'.")

        elif choice == '3':
            category = input("Enter category: ")
            items = tracker.view_items(category)
            print(f"Items in '{category}': {items}")

        elif choice == '4':
            all_items = tracker.view_all()
            print("All Items:")
            for category, items in all_items.items():
                print(f"{category}: {items}")

        elif choice == '5':
            print("Exiting tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()