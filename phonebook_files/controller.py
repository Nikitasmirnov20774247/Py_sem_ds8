from log import *
import searchcont as sarch
import delitcont as delit
import newcont as newс
import redactcont as redact

filename = 'myphonebook.txt'
myfile = open(filename, 'a+')
myfile.close

def main_menu():
    logger.debug('function call - main_menu')
    print('\nГлавное меню\n')
    print('1. Показать список контактов')
    print('2. Поиск существующего контакта')
    print('3. Добавить новый контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Выход')
    
    choice = input('Введите свой выбор: ')
    logger.info(f"user's choice: {choice}")
    if choice == '1':
        myfile = open(filename, 'r+')
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print('!! В телефонной книге нет контакта !!')
            logger.info('no data detected')
        else:
            print(filecontents)
            logger.debug('list output')
        myfile.close
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()
    elif choice == '2':
        sarch.searchcontact()
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()
    elif choice == '3':
        newс.newcontact()
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()
    elif choice == '4':
        redact.redactcontact()
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()
    elif choice == '5':
        delit.delitcontact()
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()
    elif choice == '6':
        print('Благодарим вас за использование телефонной книги!')
    else:
        print('!! Пожалуйста, предоставьте действительные входные данные !!\n')
        logger.warning('incorrect data entered')
        enter = input('Нажмите Enter, чтобы продолжить ...')
        main_menu()