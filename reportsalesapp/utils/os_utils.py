import os
import shutil


# def create_name_file(old_name: str, new_name: str) -> str:
#     temp = os.path.splitext(old_name)
#     return new_name + temp[1]


def checking_folder(link: str):
    if len(os.listdir(link)) == 0:
        return True
    else:
        return False


def enumerate_folder(link: str):
    directory = link
    lst = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            lst.append(str(f))
    return lst


def delete_file(link: str):
    try:
        os.remove(link)
        print("Файл успешно удален!")
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Произошла ошибка при удалении файла: {str(e)}")


def moove_primary_documents(link_file: str, link_dir: str):
    temp_dir = os.getcwd()
    shutil.copy(
        os.path.join(temp_dir, link_file),
        os.path.join(link_dir)
    )


def create_link_new_file(link_old_name: str, new_name: str):
    temp = repr(link_old_name).replace(r'\x0', r'\\').partition("\\\\")[2].partition('.')[0]
    link_new_name = repr(link_old_name).replace(r'\x0', r'\\').replace(temp, new_name)
    link_new_name = link_new_name.replace(r'\\\\', r'\\')[1:-1]
    return link_new_name


def rename_file(link_old_name: str, link_new_name: str):
    os.rename(link_old_name, link_new_name)
