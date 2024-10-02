class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"\nContact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            print("\nContact List:")
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")

    def search_contact(self, search_term):
        for name, phone in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in phone:
                print(f"\nContact Found: Name: {name}, Phone: {phone}")
                return
        print("\nNo contact found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact '{name}' deleted successfully!")
        else:
            print("\nContact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)
        
        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == "4":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
