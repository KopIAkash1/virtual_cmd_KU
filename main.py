import sys
from zipfile import ZipFile


def pwd():
    return Path


def ls(Path):
    for files in allFiles:
        files = "/" + files
        if (files[len(files) - 1] == "/"):
            files = files[:-1]
        if (Path in files):
            files = files[(len(Path)) - 1:]
            # print(files[:-1][1:])
            if not ("/" in files[1:]):
                print(files[1:], end=" ")
    print()


def cd(command, Path):
    if (command[1][len(command[1]) - 1] != "/"):
        command[1] += "/"
    for file in allFiles:
        if (command[1] == file):
            Path += command[1][:-1];
            return Path + "/"


def cat(Path):
    with main_file.open(Path, "r") as file:
        text = file.read().decode("utf-8")
        print(text)


# Точка старта
if __name__ == '__main__':
    # Цикл получения доступа к файлу
    a = sys.argv
    command = ""
    if (sys.argv[1] != "--script"):
        print("Error args, restart!")
        exit(-1)
    else:
        try:
            file_name = sys.argv[1]
        except:
            print("Error name! Restart!")
            exit(-2);
        main_file = ZipFile(sys.argv[2])
        print("Succses!")
    # Основной процесс программы
    Path = "/"
    rootName = "root:~"
    allFiles = main_file.namelist()

    while command != exit:
        command = input(rootName + Path[:-1] + "# ")
        command = command.split(" ")
        if (command[0] == "pwd"):
            print(pwd())
        elif (command[0] == "cd"):
            if (rootName[len(rootName) - 1] == "~"):
                rootName = rootName[:-1]
            Path = cd(command, Path)
        elif (command[0] == "ls"):
            ls(Path)
        elif (command[0] == "cat"):
            if "." in command[1]:
                cat(Path[1:] + command[1])
            else:
                print("cat: can't open '" + command[1] + "' : No such file in directory")
        else:
            print(command[0] + ": not found")
