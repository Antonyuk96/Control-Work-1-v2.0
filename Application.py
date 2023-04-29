def run():
    c = Controller(ModelJSON("notes.json"), View())

    while True:
        command = input(Fore.BLUE +
                        '1 - Добавление заметки\n'
                        '2 - Прочтение заметки\n'
                        '3 - Изменить заметку\n'
                        '4 - Удаление заметки\n'
                        '5 - Удаление всех заметок\n'
                        '6 - Прочитать все заметки\n'
                        '7 - Выйти\n' +
                        'Выбрать: '
                        + Style.RESET_ALL)
        if command == '7':
            break
        if command == '1':
            print(Fore.GREEN + '\Добавление  заметки:' + Style.RESET_ALL)
            c.create_note(get_note_data())
        elif command == '2':
            print(Fore.GREEN + '\nПрочтение заметки:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + '\Изменить заметку:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())
        elif command == '4':
            if c.notes_exist():
                print(Fore.RED + '\nУдаление заметки:' + Style.RESET_ALL)
                delete_id = int(get_number())
                if c.note_id_exist(delete_id):
                    c.delete_note(delete_id)
        elif command == '5':
            if c.notes_exist():
                print(Fore.RED + '\nУдаление всех заметок:' + Style.RESET_ALL)
                if input(Fore.RED + 'Подтверждаем удаление заметок? (Y/N): '
                         + Style.RESET_ALL).capitalize() == 'Y':
                    if c.notes_exist():
                        c.delete_all_notes()
        elif command == '6':
            if c.notes_exist():
                print(Fore.BLUE + '\Прочитать все заметки:' + Style.RESET_ALL)
                c.show_notes()
        else:
            print(Fore.RED + 'Команда не найдена' + Style.RESET_ALL)
            def get_note_data():
                while True:
                    get_choice = input('Введите id заметки: ')
                    if get_choice.isdigit() and int(get_choice) > 0:
                        return get_choice
                    else:
                        print(Fore.RED + 'Введите целое положительное число!' + Style.RESET_ALL)
                        
