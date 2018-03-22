#Problem 7 - Database and Search algorithm

#Let us create a database to store our usernames
usernames = []

#Set a status variable to determine if we are running the program or not
status = True

#Define our commands
def add(incoming_username):
    usernames.append(incoming_username)

def find(string_to_look):
    tally = 0
    for i in usernames:
        if string_to_look in i:
            tally += 1
    print(tally)

def list_of_commands():
    print("\nHere are the lists of commands:")
    print("add  x : add the element x to the database")
    print("find x : find the element x in the database")
    print("exit   : terminates the program \n")

def stop_running():
    global status
    status = False


#Store our list of commands
operations = {"add": add, "find": find, "help": list_of_commands, "exit": stop_running}

#Run the program
print("type help for lists of commands \n")
while status:
    command = input("input: ").split()
    if len(command) < 2:
        operations[command[0]]()
    else:
        if command[0] in operations:
            operations[command[0]](command[1])
        else:
            print("Command not found. Try again")
    
