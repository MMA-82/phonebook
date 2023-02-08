
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

def save_phone_book():
   print('Изменения сохранены')
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
   name = input('Введите имя: ')
   phone = input('Введите номер телефона: ')
   comment = input('Введите описание: ')
   print('Появился новый контакт! Выберите п.3, чтобы проверить')
   print()
   return name, phone, comment

def confirm_delete(del_contact):
   confirm = input(f'Вы точно хотите удалить {del_contact}? да/нет: ').lower()
   if confirm == 'да':
      return True
   else:
      return False

def fact_delete():
   print('Контакт удален! Выберите п.3, чтобы проверить')
   print()

def select_contact():
   select = input('Выберите контакт: ')
   return select

def change_contact():
   print('Введите новые данные, или пропустите, нажав Enter')
   new_name = input('Введите имя: ')
   new_phone = input('Введите номер телефона: ')
   new_comment = input('Введите описание: ')
   print()
   return new_name, new_phone, new_comment

def fact_change():
   print('Изменения внесены! Выберите п.3, чтобы проверить')
   print()
 
def empty_request():
   print('Совпадений не найдено, попробуйте еще!')
   print()

def many_request():
   print('Найдено несколько схожих контактов, введите данные точнее!')
   print()   
 
def find_contact():
   find = input('Введите искомые данные: ')
   return find

def input_error():
   print('Ошибка ввода. Введите корректный пункт меню!!!')
   print()

def exit():
   print('Книга закрыта, вы вышли из программы')

