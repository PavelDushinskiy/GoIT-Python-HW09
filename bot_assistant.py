list_of_contacts = []


class MyException(Exception):
    def __init__(self, value):
        self.value = value


def exec_hello():
    print("How can I help you?")


def exec_add(command: str):
    dict_of_contacts = {"name": command.split(" ")[1],
                        "phone": command.split(" ")[2]}
    list_of_contacts.append(dict_of_contacts)


def exec_change(command):
    for contact in list_of_contacts:
        if contact.get("name") == command.split(" ")[1]:
            contact["phone"] = command.split(" ")[2]


def exec_phone(command):
    for contact in list_of_contacts:
        if contact.get("name") == command.split(" ")[1]:
            print(f'Phone: {contact.get("phone")}')


def exec_show_all():
    for contact in list_of_contacts:
        print(f'Name: {contact.get("name")}: {contact.get("phone")}')


def input_error(func):
    def wrapped():
        while True:
            try:
                return func()
            except MyException as e:
                print(e)

    return wrapped


@input_error
def main():
    while True:
        command = input("? ")
        if command.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            raise SystemExit
        elif command.lower() == "hello":
            exec_hello()

        elif command.split(" ")[0].lower() == "add":
            if len(command.split(" ")) < 2:
                raise MyException("Give me name and phone please")
            else:
                exec_add(command)

        elif command.split(" ")[0].lower() == "change":
            if len(command.split(" ")) < 2:
                raise MyException("Give me name and phone please")
            else:
                exec_change(command)

        elif command.split(" ")[0].lower() == "phone":
            if len(command.split(" ")) < 2:
                raise MyException("Enter user name please")
            exec_phone(command)

        elif command.lower() == "show all":
            if len(list_of_contacts) == 0:
                raise MyException("The list of contacts is empty")
            exec_show_all()


if __name__ == "__main__":
    main()
