
# функция для создания файла
import os
import datetime
import shutil


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError as d:
        print('МОжно двигаться дальше ', d)


def info_path(fol_only=False):
    result = os.listdir()
    # result1 = os.listdir()
    if fol_only:
        result = [f for f in result if os.path.isdir(f)]

    print(f'=====>{result}')
    # print(result1)


def del_ff(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_ff(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)

        except FileExistsError as a:
            print(f'====>уже  {a}')

    else:
        shutil.copy(name, new_name)

def save_data(massege):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massege}'
    print(f'===> {result}')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{result}\n')

# что бы в другом м, одуле не запускался код
if __name__ == '__main__':
    create_file('text.txt', 'eeeee')

    create_file('text.js', 'some text')
    create_folder('new_folder3')
    del_ff('text.js')
    info_path(False)
    copy_ff('new_folder2', 'new_name_folder4')
    copy_ff('text.txt', 'text.txt1')
    save_data('asd')
