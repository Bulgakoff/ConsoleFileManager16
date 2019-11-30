# функция для создания файла
import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError as d:
        print('МОжно двигаться дальше ', d)


def info_path():
    result = os.listdir()
    # result1 = os.listdir()

    result = [f for f in result if os.path.isdir(f)]

    print(f'=====>{result}')
    # print(result1)
def del_ff(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)




# что бы в другом модуле не запускался код
if __name__ == '__main__':
    create_file('text.js')
    create_file('text.js', 'some text')
    create_folder('new_folder2')
    del_ff('text.js')
    info_path()
