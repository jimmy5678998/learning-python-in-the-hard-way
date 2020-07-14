from sys import argv

script, filename = argv
a = True
while a:
    print(f"We're going to read {filename}")
    print("Type \"Yes\" if you want to read.")
    print("Type \"No\" if you don't want.")
    choice = input("> ")

    if choice == "No":
        a = False
        break
    if choice != "No" or "Yes":
        print("Please input the correct word to indicate your preference.")
    if choice == "Yes":
        print("Opening the file...")
        txt = open(filename)
        print("Here's your file content:")
        print(txt.read())
        txt.close()
        break



