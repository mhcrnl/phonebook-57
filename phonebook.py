import pickle
phone_book = pickle.load( open( "phone.p", "rb" ) )
def add(nama=None):
    print(phone_book)
    if not nama:
        nama = input("Name? ")
    if nama not in phone_book:
        number = input("Phone number? ")
        phone_book[nama] = number
    elif nama in phone_book:
        print ("Name already existed. The number is " + phone_book[nama])
    pickle.dump(phone_book, open( "phone.p", "wb" ) )
def update():
    nama = input("Name? ")
    if nama not in phone_book:
        print(nama, "doesn't exist yet. \nAdding", nama, "into the phone book.")
        add(nama)
    elif nama in phone_book:
        print("Name found.")
        number = input("Please enter the new phone number:")
        phone_book[nama] = number
        pickle.dump(phone_book, open( "phone.p", "wb" ) )

command = input("What would you like to do?")
while command:
    if "add" in command.lower():
        add()
    elif "update" in command.lower():
        update()
    command = input("What would you like to do?")
    
