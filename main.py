savepath = "save.txt"

def read():
    with open(savepath, "r") as journal:
        read_journal = journal.read()
    print(read_journal)

def add_entry():
    userinput2 = input("input the name of your entry: ")
    userinput3 = input("input your entry: ")
    with open(savepath, "a") as journal:
        journal.write("\n" + userinput2 + "\n" + userinput3 + "\n")

while True:
    print("""Menu:
    1) read journal
    2) add entry
    3) quit""")
    userinput = input("input your choice: ").strip()

    match(int (userinput)):
        case 1:
            read()
        case 2:
            add_entry()
        case 3:
            break
        case _:
            print("error")