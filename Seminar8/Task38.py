import os


def show_contact(file_name):
    os.system('clear')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')

    input('\nДля продолжения нажмите Enter')


def add_contact(file_name):
    with open(file_name, 'a') as file:
        res = ''
        res += input('Введите фамилию контакта: ')
        res += input('Введите имя контакта: ')
        res += input('Введите телефон контакта: ')

        file.write('\n' + res)

    input('Для продолжения нажмите любую клавишу')


def search_contact(file_name):
    target = input('Введите имя контакта для поиска: ')

    with open(file_name, 'r') as file:
        data = file.readlines()
        file.seek(0)

        if target in file.read():
            for contact in data:
                if target in contact:
                    print(contact)
                    break
        else:
            print('Данного контакта не существует')

        input('Для продолжения нажмите Enter')


def delete_contact(file_name):
    os.system('clear')
    target = input('Введите имя контакта для удаления: ')

    with open(file_name, 'r') as file:
        file.seek(0)
        data = file.readlines()
        file.seek(0)
        contacts = file.read()

        if target == '' or target == ' ':
            print('Данного контакта не существует1')
        elif target in contacts:
            file.seek(0)
            for contact in data:
                if target in contact:
                    contacts = contacts.replace(contact, '')
                    break
            with open(file_name, 'w') as file_add:
                file_add.write(contacts)
                print('Удаление контакта успешно завершено')
        else:
            print('Данного контакта не существует')

    input('Для продолжения нажмите Enter')


def edit_contact(file_name):
    os.system('clear')
    target = input('Введите имя контакта для изменения: ')

    with open(file_name, 'r') as file:
        file.seek(0)
        data = file.readlines()
        file.seek(0)
        contacts = file.read()

        if target == '' or target == ' ':
            print('Данного контакта не существует')
        elif target in contacts:
            file.seek(0)
            for contact in data:
                if target in contact:
                    print('Какие данные вы хотите изменить?')
                    print('1 - фамилию')
                    print('2 - имя')
                    print('3 - телефон')
                    user_edit = int(input('Введите код действия от 1 до 3: '))
                    if user_edit == 1:
                        user_text = input('Введите новую фамилию контакта: ')
                        file.seek(0)
                        contacts = contacts.replace(contact.split()[0], user_text)
                        break
                    elif user_edit == 2:
                        user_text = input('Введите новое имя контакта: ')
                        file.seek(0)
                        contacts = contacts.replace(contact.split()[1], user_text)
                    elif user_edit == 3:
                        user_text = input('Введите новый телефон контакта: ')
                        file.seek(0)
                        contacts = contacts.replace(contact.split()[2], user_text)
            with open(file_name, 'w') as file_add:
                file_add.write(contacts)
                print('Контакт успешно изменен')
        else:
            print('Данного контакта не существует')

    input('Для продолжения нажмите Enter')


def drawing():
    print('Добрый день! Выберите действие. \n')
    print('1 - показать контакты')
    print('2 - добавить контакт')
    print('3 - найти контакт')
    print('4 - удалить контакт')
    print('5 - изменить контакт')
    print('6 - выйти из программы')


def main(file_name):
    while True:
        os.system('clear')
        drawing()
        user_choice = int(input('Введите номер команды от 1 до 6: '))
        match user_choice:
            case 1:
                show_contact(file_name)
            case 2:
                add_contact(file_name)
            case 3:
                search_contact(file_name)
            case 4:
                delete_contact(file_name)
            case 5:
                edit_contact(file_name)
            case 6:
                os.system('clear')
                print('Работа программы была завершена. Хорошего дня!')
                exit()
            case _:
                print('Данная команда не найдена')
                input('Для продолжения нажмите Enter')


main('Contacts.txt')
