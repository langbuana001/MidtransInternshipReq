class Person:

    def __init__(self, transact, email, phone, card):
        self.transactions = [transact]
        self.emails = [email]
        self.phones = [phone]
        self.cards = [card]

    def get_transactions(self):
        return self.transactions

    def get_emails(self):
        return self.transactions

    def get_phones(self):
        return self.transactions

    def get_cards(self):
        return self.transactions

    def add_transaction(self, transaction):
        if transaction in self.transactions:
            pass
        else:
            self.transactions.append(transaction)

    def add_email(self, email):
        if email in self.emails:
            pass
        else:
            self.emails.append(email)

    def add_phone(self, number):
        if number in self.phones:
            pass
        else:
            self.phones.append(number)

    def add_card(self, card):
        if card in self.cards:
            pass
        else:
            self.cards.append(card)

    def display_info(self):
        print("Customer : \n transactions:", self.transactions,"\n emails      :", self.emails, "\n phones      :", self.phones, "\n cards       :", self.cards,  "\n")
















