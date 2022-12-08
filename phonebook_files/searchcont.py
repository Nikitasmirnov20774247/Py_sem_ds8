import controller as con

def searchcontact():
    con.logger.debug('function call - searchcontact')
    print('\nМеню поиска\n')
    print('1. Поиск по Ф.И.О')
    print('2. Поиск по номеру телефона')
    print('3. Поиск по email')
    print('4. Выход в главное меню')
    
    search = ''
    choice = input('Введите свой выбор: ')
    con.logger.info(f"user's choice: {choice}")
    if choice == '1':
        print('Данные вводить на англиском')
        search = input('Введите имя / фамилия / отчество: ')
        search = search.title()
    elif choice == '2':
        search = input('Введите номер телефона: ')
    elif choice == '3':
        print('Данные вводите на англиском')
        search = input( 'Введите email: ')
        remname = search[1:]
        firstchar = search[0]
        search = firstchar.lower() + remname
    elif choice == '4':
        print('Возвращаемся в главное меню')
        con.main_menu()
    else:
        print('!! Пожалуйста, предоставьте действительные входные данные !!\n')
        enter = input('Нажмите Enter, чтобы продолжить ...')
        searchcontact()

    myfile = open(con.filename, 'r+')
    filecontents = myfile.readlines()
    con.logger.info(f'open and read the file: {con.filename}')

    found = False
    for line in filecontents:
        if search in line:
            print(f'Ваша контактная информация - это: {line}')
            found = True
    if found == False:
        print(f'Искомый контакт недоступен в телефонной книге: {search}')
        con.logger.warning(f'contact not found: {search}')

    myfile.close
    con.logger.debug(f'close file: {con.filename}')