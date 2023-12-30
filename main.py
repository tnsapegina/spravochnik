# Открыть фаил
# Сохранить фаил
# Создание контакта
# Изм контакта
# Найти контакт
# Удалить контакт
# Показать контакт
# выход

def print_menu():
    print("1. Create contact")
    print("2. Change contact")
    print("3. Find contact")
    print("4. Delete contact")
    print("5. Show contact")
    print("6. Exit")


def get_input_contact(file_name):
    count = count_contact(file_name)
    information = list()
    information.append(str(count))
    information.append(input("Введите имя контакта: "))
    information.append(input("Введите номер контакта: "))
    information.append(input("Введите ник контакта: "))
    return information


def count_contact(file_name):
    with open(file_name, 'r') as fp:
        return sum([1 for line in fp])
    
def create_contact(file_name):
    contact = get_input_contact(file_name)

    with open(file_name, "a") as file:
        file_name(";".join(contact) + "\n")

def show_contact(file_name):
    with open(file_name, "r") as file:
        for line in file:
          print(line, end=" ")

def change_contact(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        
    for line in lines:
        print(line, end=" ")

    id_for_change = int(input("Введите индекс контакта для изменения:"))
    if 0 <= len(lines):
        contact = get_input_contact(file_name)
        contact[0] = str(id_for_change)
        contact = ";".join(contact) + "\n"
        lines[id_for_change] = contact

    with open(file_name, "w") as file:
        file.writelines(lines)

def find_contact(file_name):
    name = input("Введите имя человека: ")
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        if name in line:
            print(line)

def delete_contact(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line, end=" ")
        
    id_for_change = int(input("Введите индекс контакта для изменения:"))
    if 0 <= id_for_change <= len(lines):
        del lines[id_for_change]
    with open(file_name, "w") as file:
        file.write(lines)


def main():
    file_name = "contacts.txt"
    while True:
        print_menu()
        input_number = int(input("Что вы выбираете?"))
        if input_number == 1:
            create_contact(file_name)
        elif input_number == 2:
            change_contact(file_name)
        elif input_number == 3:
            find_contact(file_name)
        elif input_number == 4:
            delete_contact(file_name)
        elif input_number == 5:
            show_contact(file_name)
        elif input_number == 6:
            break
    print("Спасибо за работу с нашим справочником!")

if __name__ == "__main__":
    main()# spravochnik1
