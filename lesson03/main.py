import sys
from core import create_file, create_folder, info_path, del_ff, copy_ff, save_data

save_data('Старт')

command = sys.argv[1]
if command == 'list':
    info_path()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError as d:
        print(f'==нет параметра =>{d}')
    else:
        create_file(name)

elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError as f:
        print(f'--нет  имени папки -->{f}')
    else:
        print('все хорошо ')
        create_folder(name)

elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError as c:
        print(f'--нет параметра --->{c}')
    else:
        print('all right ')
        del_ff(name)

elif command == 'copy':

    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError as g:
        print(f'====>{g}')
    else:
        print('all right!!!!!!!!!!!!!!!')
        copy_ff(name, new_name)
elif command == 'help':
    print('помощь')

save_data('конец')