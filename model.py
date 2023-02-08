import controller
import view

phone_book = []
path = 'phone_book.txt'

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))

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

def add_new_contact(new_contact):
    global phone_book
    phone_book.append(new_contact)

def remove_contact(del_contact):
    global phone_book
    phone_book.remove(del_contact)

def rename_contact(select):
    global phone_book
    result = []
    for j, cont in enumerate(phone_book):
        for field in cont:
            if select in field:
                result.append((cont, j))
                break
    if len(result) > 1:
        return False
    elif result == []:
        return result
    else:
        return result[0]

def update_contact(index, new):
    global phone_book
    phone_book[index][0] = new[0] if new[0] != '' else phone_book[index][0]
    phone_book[index][1] = new[1] if new[1] != '' else phone_book[index][1]
    phone_book[index][2] = new[2] if new[2] != '' else phone_book[index][2]


def search_contact(find):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def close_file():
    global phone_book
    global path
    data = open('phone_book.txt', 'r')
    data.close()


    