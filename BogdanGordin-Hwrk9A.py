"""
    Emails
    Bogdan Gordin
    October 23, 2017
    COMSC-122-0940
    Mr. Littlefield

Below are notes:

    *Ouch. physics is tough.

"""

import pickle
import os

def main():
    try:
        print("\n\tCoocoo. This is Bogdan's Gordin Wackhy Emails program.")

        print("Sometimes I dream about cheese...")


        wackhyEmails = {}
        if os.path.isfile('myWackhyEmails.dat'):
            wackhyEmails = load()

        usersChoice = 0

        while usersChoice != 6:

            displayMainMenu()
            usersChoice = int(input('Enter your menu: '))

            while usersChoice > 6:
                usersChoice = int(input('Try again: '))
            
            if usersChoice == 1:
                lookUpEmail(wackhyEmails)

            elif usersChoice == 2:
                addEmail(wackhyEmails)

            elif usersChoice == 3:
                changeEmail(wackhyEmails)

            elif usersChoice == 4:
                deleteEmail(wackhyEmails)

            elif usersChoice == 5:
                saveEdits(wackhyEmails)


        print("\n\n\n...")
        exit = input('Please "Le Brie cheese is fine, but Galbani is better." any key botton to Exit: ')
    except Exception as oops:
        print("\n", oops)
        print("\n\n\n...")
        exit = input('Please "Le Brie cheese is good, but Galbani is better." any key botton to Exit: ')


def displayMainMenu():
    print()
    print("Main Menu.")
    #print('1) Display emails.')
    print('1) Look up email.')
    print('2) Add new email.')
    print('3) Change an email.')
    print('4) Delete an email.')
    print('5) Save Updated emails.')
    print('6) Quit the program.')
    print()


def lookUpEmail(wackhyEmails):
    user = input('Enter a name: ')

    print(wackhyEmails.get(user, 'None found.'))
    print("\n")


def addEmail(wackhyEmails):
    user = input('Enter the user name: ')
    email = input("User's email: ")

    if user not in wackhyEmails:
        wackhyEmails[user] = email
    else:
        print('WOW. This already exists.')


def changeEmail(wackhyEmails):
    user = input('Enter the user name: ' )
    email = input("User's email: ")

    if user in wackhyEmails:
        wackhyEmails[user] = email
    else:
        print('Not found.')


def deleteEmail(wackhyEmails):
    user = input('Enter a name: ')

    if user in wackhyEmails:
        del wackhyEmails[user]
    else:
        print('Nothing found.')


def saveEdits(wackhyEmails):
    output_file = open('myWackhyEmails.dat', 'wb')
    pickle.dump(wackhyEmails, output_file)
    output_file.close()


def load():
    temp = {}
    end_of_file = False
    infile = open('myWackhyEmails.dat', 'rb')
    while not end_of_file:
        try:
            temp = pickle.load(infile)
        except EOFError:
            end_of_file = True
    infile.close()
    return temp

"""
def ord_shift(s, x):
    return ''.join(map(lambda c: chr(ord(c)+x), s))

def encipher(msg):
    return ord_shift(msg, 1)

def decipher(msg):
    return ord_shift(msg, -1)
"""
main()


