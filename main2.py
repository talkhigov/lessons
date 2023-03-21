import sys
from lesson14 import save_info, get_list, delete_file, copy_file, creat_folder, create_file

save_info('start')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название папки')
    else:
        creat_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название файла или папки')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('отсутствует название копируемого файла или папки')
    try:
        new_name = sys.argv[3]
    except IndexError:
        print('отсутствует новое название файла или папки')
    else:
        copy_file(name, new_name)
elif command == 'game':
    from lesson7_pz_1 import*
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('game - игра - угадай слово')

save_info('end')