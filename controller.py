import model
import view

def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
            view.open_phone_book()
        
        elif choice == 2:
            model.save_file()
            view.save_phone_book()
        
        elif choice == 3:
            view.show_contacts(model.get_phone_book())
        
        elif choice == 4:
            #new_contact = list(view.create_new_contact())
            model.add_new_contact(list(view.create_new_contact()))
        
        elif choice == 5:
            #deleted = view.delete_contact()
            del_contact = model.search_contact(view.select_contact())
            if len(del_contact) == 1:
                confirm = view.confirm_delete(del_contact[0][0])
                if confirm:
                    model.remove_contact(del_contact[0])
                    view.fact_delete()
            elif del_contact == []:
                view.empty_request()
            else:
                view.many_request()
              
        elif choice == 6:
            #select = view.select_contact()
            rename = model.rename_contact(view.select_contact())
            if rename:
                #changed = view.change_contact()
                model.update_contact(rename[1], list(view.change_contact()))
                view.fact_change()
            elif rename == []:
                view.empty_request()
            else:
                view.many_request()
        
        elif choice == 7:
            #find = view.find_contact()
            result = model.search_contact(view.find_contact())
            if result:
                view.show_contacts(result)
            else:
                view.empty_request()
        
        elif choice == 8:
            model.close_file()
            view.exit()
            break
        else:
            view.input_error()
    
            