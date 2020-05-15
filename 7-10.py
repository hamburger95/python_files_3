# 7.
def call_file(user_name):
    try:
        f = open("words.txt", "a", encoding="utf-8")
    except IOError:
        print("something went wrong when trying to open words.txt")

    try:
        f.write("\n" + user_name)
    except IOError:
        print("something went wrong when trying to write into file")

    try:
        f = open("words.txt", "r", encoding="utf-8")
        file_content = f.readlines()
        for line in file_content:
            print(line)
    except IOError:
        print("something went wrong when trying to read file")
    finally:
        f.close()


def get_name():
    name = input("Please enter your name and press enter: ")
    call_file(name)


get_name()
