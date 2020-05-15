
def get_name():
    name = input("Please enter your name: ")
    add_name(name)


def add_name(Name):
    my_new_file = open("name.txt", "a")
    my_new_file.write("\nHello " + Name)
    my_new_file.close()

def print_names():
    name_txt = open("name.txt", "r")
    print_names()

for i in range(5):
    get_name()
