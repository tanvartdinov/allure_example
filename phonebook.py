class PhoneBook:
    def __init__(self, contacts=None):
        if contacts is None:
            contacts = {}
        self.contacts = {k.lower(): v for k,v in contacts.items()}

    def __iter__(self):
        self.names = list(self.contacts.keys())
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.names):
            raise StopIteration
        name = self.names[self.counter]
        phone = self.contacts[name]
        return f'{name.capitalize():20} {phone}'

    def add_contact(self, name, phone):
        self.contacts[name.lower()] = phone

    def find_contact(self, name):
        name_ic = name.lower()
        for contact, phone in self.contacts.items():
            if name_ic in contact:
                return phone
        return None

    def get_all_contacts(self):
        return self.contacts


if __name__ == '__main__':
    phonebook = PhoneBook()
    phonebook.add_contact('Мама', 124124124)
    phonebook.add_contact('папа', 999999999)
    phonebook.add_contact('братан', 345345623)
    phonebook.add_contact('Васек', 457373434)
    phonebook.add_contact('ПАПА', 888888888)

    for contact in phonebook:
        print(contact)