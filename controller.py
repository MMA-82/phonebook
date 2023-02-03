import model
import view

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
        elif choice == 2:
            model.save_file()
        elif choice == 3:
            view.show_contacts(model.get_phone_book())
        elif choice == 4:
            new_contact = list(view.create_new_contact())
            model.add_new_contact(new_contact)
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            find = view.find_contact()
            result = model.search_contact(find)
            view.show_contacts(result)
        else:
            view.input_error()
            