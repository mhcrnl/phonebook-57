import pickle
phone_book = pickle.load( open( "phone.p", "rb" ) )
def add(nama=None):
    #add a new contact.
    if not nama:
        nama = input("Insert name: ")
    if nama not in phone_book:
        number = input("Please enter "+ nama + "'s phone number: ")
        phone_book[nama] = number
        pickle.dump(phone_book, open( "phone.p", "wb" ) )
        print(nama, "is successfully added into the phonebook.")
    elif nama in phone_book:
        print ("Name already existed. The number is " + phone_book[nama])
   
def update():
    #update contact's number.
    nama = input("Insert name: ")
    if nama not in phone_book:
        print(nama, "doesn't exist yet. \nAdding", nama, "into the phone book.")
        add(nama)
    elif nama in phone_book:
        print("Name found. The existing number is " + phone_book[nama])
        number = input("Please enter the new phone number:")
        phone_book[nama] = number
        pickle.dump(phone_book, open( "phone.p", "wb" ) )
        
def printing():
    #print all contacts and their phone numbers.
    phone_book = pickle.load( open( "phone.p", "rb" ) )
    phonelist = list(phone_book.items())
    print(phonelist)
    print("Name\t|Phone Number")
    print("-"*21)
    for name,number in phonelist:
        print("{0}\t|{1}".format(name,number))

def delete_all():
    #delete all contacts.
    phone_book = {}
    pickle.dump(phone_book, open( "phone.p", "wb" ) )
    printing()    

command = input("What would you like to do? (press Enter to terminate)")
while command:
    if "add" in command.lower():
        add()
    elif "update" in command.lower():
        update()
    elif "print" in command.lower():
        printing()
    elif "delete all" in command.lower():
        delete_all()
    command = input("What would you like to do? (press Enter to terminate)")

