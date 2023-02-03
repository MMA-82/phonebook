
phone_book = []
path = 'phone_book.txt'

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split('-'))

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))

def get_phone_book():
    global phone_book
    return phone_book

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)


def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for item in contact:
            if find in item:
                result.append(contact)
                break
    return result

    