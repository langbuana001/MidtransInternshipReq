#Problem 2 - Pattern Matching and Grouping
#See Note Below

from collections import *
from Person import *

number_of_transaction = 0
email_list = []
phone_list = []
card_list  = []

ledger = []
person = []

#Find the first element occurence,
#   we can infer that when found, this is the moment
#   the Person class was created, giving its index in person[]
def identify_person_index(value, input_list):

    index = 0
    for i in input_list:
        if i == value:
            return index
        else:
            index += 1
    return None
    

running = True
while running:
    email_list.append(input("Enter email :"))
    phone_list.append(input("Enter phone :"))
    card_list.append(input("Enter card  :"))
    print("Transaction Recorded!\n")
    
    number_of_transaction += 1
    ledger.append({'id': number_of_transaction, 'email': email_list[-1], 'phone': phone_list[-1], 'card': card_list[-1]})

    #Let the first transaction set its shop
    if number_of_transaction < 2:
        person.append(Person(number_of_transaction,email_list[-1],phone_list[-1],card_list[-1]))
    else:
        if email_list.count(email_list[-1]) == 1 and phone_list.count(phone_list[-1]) == 1 and card_list.count(card_list[-1]) == 1:
            #New Person, create profile
            person.append(Person(number_of_transaction,email_list[-1],phone_list[-1],card_list[-1]))
        else:
            #Merge the elements
            #Detect any simmilarities
            if email_list.count(email_list[-1]) > 1 or phone_list.count(phone_list[-1]) > 1 or card_list.count(card_list[-1]) > 1:
                #identify the individual
                index = [identify_person_index(email_list[-1], email_list), identify_person_index(phone_list[-1], phone_list), identify_person_index(card_list[-1], card_list)]
                if len(index) > 0:
                    index = index[0]
                    
                person[index].add_transaction(number_of_transaction)
                person[index].add_email(email_list[-1])
                person[index].add_phone(phone_list[-1])
                person[index].add_card(card_list[-1])
                    
                


    for i in person:
        i.display_info()


#Ran out of time.
"""
    Potential fix implementation:
    I recognize that this can be solved using the union set operation,
    as it is perfect for this kind of problem.
"""
















    
