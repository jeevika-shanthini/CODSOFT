contacts={}

while True:
    print("="*50)
    print("\n       CONTACT BOOK MENU")
    print("="*50)
    print("1. create Contact")
    print("2. View Contacts")       
    print("3. update Contact")
    print("4. Delete Contact")
    print("5. search Contact")
    print("6. count Contact")
    print("7. Exit")
    print("="*50)
    Choice = input("Enter your choice (1-7): ")
    if Choice == '1':
        print("\n-------CREATE CONTACT-------")
        name = input("Enter contact name: ")
        if name in contacts:
            print(f"Contact name {name} already exists.")
        else:
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact name {name} has been created successfully!.")    

    elif Choice == '2':
        print("\n-------VEIW CONTACT-------")
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Contact name: {name}")
            print(f"Phone number: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        else:
            print(f"Contact name {name} not found!.")

    elif Choice == '3':
        print("\n-------UPDATE CONTACT-------")
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new contact phone number: ")
            email = input("Enter new contact email: ")
            address = input("Enter new contact address: ")
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact name {name} has been updated successfully!.")
        else:
            print(f"Contact name {name} not found!.")

    elif Choice == '4':
        print("\n-------DELETE CONTACT-------")
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully!.")
        else:
            print(f"Contact name {name} not found!")

    elif Choice == '5':
        print("\n-------SEARCH CONTACT-------")
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Contact name: {name}")
                print(f"Phone number: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True

        if not found:
            print(f"No contacts found matching '{search_name}'!")
    elif Choice == '6':
        print("\n-------CONTACT COUNT-------")
        count = len(contacts)
        print(f"Total number of contacts: {count}")
    elif Choice == '7':
        print("="*50)
        print("Thank you for using the Contact Book")
        print(" Goodbye!")
        print("="*50)
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")        