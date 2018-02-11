#Created by Gilbert Vincenta
import pickle
EMAIL_ATTRIBUTES = "ABCDEFGHIJKLMNOPQRTSUVWXYZ@.1234567890" #based on Gmail's rule of email account's name.
phone_book = pickle.load( open( "phone.p", "rb" ) )
def verify_email(email):
    alpha = True
    re_enter = False
    while alpha:
        for char in email:
            if char.upper() not in EMAIL_ATTRIBUTES:
                email = input("Please re-enter the email: ")
                re_enter = True
                break
        if not re_enter:
            alpha = False

def insert(nama, number, email = None):
    #insert into phone book.
    while ( "+" not in number or not (number[1:].isdigit()) or not (11 <= len(number) <= 13) ): #phone number verification
        number = input("Please re-enter the number: ")
    verify_email(email)
    data = [number, email]
    phone_book[nama] = data
    pickle.dump(phone_book, open( "phone.p", "wb" ) )

def add(nama=None):
    #add a new contact.
    if not nama:
        nama = input("Insert name: ")
    if nama not in phone_book:
        number = input("Please enter "+ nama + "'s phone number: ")
        email = input("Please enter "+ nama + "'s email: ")
        insert(nama, number, email)
        print(nama, "is successfully added into the phonebook.")
    elif nama in phone_book:
        print ("Name already existed. The number is " + phone_book[nama][0])
   
def update():
    #update contact's number.
    nama = input("Insert name: ")
    if nama not in phone_book:
        print(nama, "doesn't exist yet.\nAdding", nama, "into the phone book.")
        add(nama)
    elif nama in phone_book:
        print("Name found. The existing number is " + phone_book[nama][0])
        print("The existing email is " + phone_book[nama][0])
        number = input("Please enter the new phone number:")
        insert(nama, number)
        
def printing():
    #print all contacts and their phone numbers.
    phone_book = pickle.load( open( "phone.p", "rb" ) )
    phonelist = list(phone_book.items())
    print("Name\t|Phone Number")
    print("-"*21)
    for name,number in phonelist:
        print("{0}\t|{1}".format(name,number))
    if not phonelist:
        print("None\t|None")

def delete(nama):
    #delete a contact.
    try:
        del phone_book[nama]
        pickle.dump(phone_book, open( "phone.p", "wb" ) )
    except KeyError:
        print(nama,"does not exist in the phone book.")
def delete_all():
    #delete all contacts.
    phone_book = {}
    pickle.dump(phone_book, open( "phone.p", "wb" ) )
    printing()

def help():
    #display instructions to users.
    print("Press Enter to terminate.")
    print("'add' to add a new contact.")
    print("'update' to update a contact's number.")
    print("'search' to search through the contact list.")
    print("'delete' to delete a contact.")
    print("'delete all' to delete all contacts.")
command = input("What would you like to do? (press Enter to terminate)\nType 'help' to display all commands.\n")

def search():
    keyword = input("Insert name: ")
    name_array = []
    counter = 1
    print("No.\t|Name\t\t|Phone Number")
    for name in phone_book:
        if keyword in name:
            name_array.append(name)
            print("{0}.\t|{1}\t|{2}".format(counter,name,phone_book[name]))
            counter += 1
    return name_array

def blackout():
    pass
while command:
    #run the selected function.
    if "add" in command.lower():
        add()
    elif "update" in command.lower():
        update()
    elif "print" in command.lower():
        printing()
    elif "delete" in command.lower():
        if "all" in command.lower():
            answer = input('Are you sure (Y/N): ')
            if answer.upper() == 'Y':
                delete_all()
                print("Restarting.\nPlease re-run the program.")
                break
        else:
            nama = input("Insert name: ")
            delete(nama)
    elif "help" in command.lower():
        help()
    elif "search" in command.lower():
        search()
    elif "b" in command.lower():
        blackout()
    command = input("What would you like to do? (press Enter to terminate) ")

