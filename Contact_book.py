import os

FILE_NAME = "contacts_data.txt"

def load_contacts():
    contacts = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    contacts.append({
                        "name": parts[0],
                        "phone": parts[1],
                        "email": parts[2],
                        "address": parts[3]
                    })
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for c in contacts:
            file.write(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}\n")

def add_contact():
    print("\n🆕 Add New Contact")
    name = input("Name     : ").strip()
    phone = input("Phone    : ").strip()
    email = input("Email    : ").strip()
    address = input("Address  : ").strip()
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        print("✅ Contact added.")
    else:
        print("⚠️  Name and phone required.")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
    else:
        print("\n📒 All Contacts:")
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} | {c['phone']}")

def search_contact():
    query = input("\n🔍 Search by name or phone: ").strip().lower()
    found = False
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print(f"\nMatch Found:\nName   : {c['name']}\nPhone  : {c['phone']}\nEmail  : {c['email']}\nAddress: {c['address']}")
            found = True
    if not found:
        print("❌ No matching contact found.")

def update_contact():
    view_contacts()
    try:
        index = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Leave field empty to keep current value.")
            current = contacts[index]
            name = input(f"Name ({current['name']}): ").strip() or current['name']
            phone = input(f"Phone ({current['phone']}): ").strip() or current['phone']
            email = input(f"Email ({current['email']}): ").strip() or current['email']
            address = input(f"Address ({current['address']}): ").strip() or current['address']
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            print("✅ Contact updated.")
        else:
            print("❗ Invalid contact number.")
    except ValueError:
        print("❗ Invalid input.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("\nEnter serial number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"🗑️  Deleted: {deleted['name']}")
        else:
            print("❗ Invalid number.")
    except ValueError:
        print("❗ Enter a valid number.")

def menu():
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

contacts = load_contacts()

while True:
    menu()
    choice = input("Choose (1-6): ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("👋 Exiting Contact Book.")
        break
    else:
        print("🚫 Invalid option.")
