
commands = ['Открыть файл', 
            'Сохранить файл', 
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
   choice = int(input('Выберете пункт меню: '))
   return choice

def show_contacts(phone_list: list):
   if len(phone_list) < 1:
      print('Телефонная книга не открыта или пустая')
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
   find = print('Введите искомый элемент контакта: ')
   return find

def input_error():
   print('Ошибка ввода. Введите корректный пункт меню!!!')

