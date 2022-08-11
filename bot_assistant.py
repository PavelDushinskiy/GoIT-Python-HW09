list_of_contacts = []


class MyException(Exception):
    def __init__(self, value):
        self.value = value


def input_error(func):
    def wrapped(*arcs):
        try:
            return func(*arcs)
        except MyException as e:
            print(e)
    return wrapped


def exec_hello():
    print("How can I help you?")


@input_error
def exec_add(command: str):
    if len(command.split(" ")) < 2:
        raise MyException("Give me name and phone please")
    else:
        dict_of_contacts = {"name": command.split(" ")[1],
                            "phone": command.split(" ")[2]}
        list_of_contacts.append(dict_of_contacts)


@input_error
def exec_change(command):
    if len(command.split(" ")) < 2:
        raise MyException("Give me name and phone please")
    else:
        flag_exist_name = 0
        for contact in list_of_contacts:
            if contact.get("name", None) == command.split(" ")[1]:
                flag_exist_name = 1
                break
        if flag_exist_name == 0:
            raise MyException(f'The name {command.split(" ")[1]} not exist')
        else:
            for contact in list_of_contacts:
                if contact.get("name") == command.split(" ")[1]:
                    contact["phone"] = command.split(" ")[2]


@input_error
def exec_phone(command):
    if len(command.split(" ")) < 2:
        raise MyException("Enter user name please")
    else:
        for contact in list_of_contacts:
            if contact.get("name") == command.split(" ")[1]:
                print(f'Phone: {contact.get("phone")}')


@input_error
def exec_show_all():
    if len(list_of_contacts) == 0:
        raise MyException("The list of contacts is empty")
    else:
        for contact in list_of_contacts:
            print(f'Name: {contact.get("name")}: {contact.get("phone")}')


def main():
    while True:
        command = input("? ")
        if command.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            raise SystemExit
        elif command.lower() == "hello":
            exec_hello()
        elif command.lower()[:3] == "add":
            exec_add(command)
        elif command.lower()[:6] == "change":
            exec_change(command)
        elif command.lower()[:5] == "phone":
            exec_phone(command)
        elif command.lower() == "show all":
            exec_show_all()


if __name__ == "__main__":
    main()
