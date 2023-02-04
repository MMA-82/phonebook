

commands = ['Открыть книгу', 
            'Сохранить книгу', 
            'Показать все контакты', 
            'Создать контакт', 
            'Удалить контакт', 
            'Изменить контакт', 
            'Найти контакт', 
            'Выход из программы']

def main_menu():
   print('Главное меню:')
   for i, item in enumerate(commands, 1):
      print(f'\t{i}. {item}')
   choice = input('Выберете пункт меню: ')
   if choice.isdigit():
       choice = int(choice)
       return choice

def open_phone_book():
   print('Вы открыли телефонную книгу')
   print()
 
def show_contacts(phone_list: list):
   if len(phone_list) < 1:
      print('Телефонная книга не открыта или пустая')
      print()
   else:
      print()
      for i, contact in enumerate(phone_list, 1):
         print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
      print()

def create_new_contact():
   name = print('Введите имя: ')
   phone = print('Введите номер телефона: ')
   comment = print('Введите описание: ')
   return name, phone, comment
   


def find_contact():
   find = str(print('Введите искомый элемент: '))
   return find

def input_error():
   print('Ошибка ввода. Введите корректный пункт меню!!!')
   print()

def exit():
   print('Книга закрыта, вы вышли из программы')

