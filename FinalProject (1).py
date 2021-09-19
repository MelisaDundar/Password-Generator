#!/usr/bin/env python
"""
Final project for UC Berkeley CS10 - Secure Password Generator.

to run the program from terminal type: python3 Final_Project.py
"""


import random
import string
import datetime
from tkinter import *

# This function is the main random number random_pw_generator
# I imported the "random" module which is is used to randomize all the different
# characters bellow
# the string import is used to sift through a list of letters which include all
# upper and lower case ran_letters1
# the inputs are min length, and max length, and must_include1, and must_include2
# when the random button is pressed, the min lenght is predetrmined, and the max pw_length
# is randomized so when we choose random it creates a random lenght each time,
# but the range keeps it from going somewhere bellow 8 or above 13.
def random_pw_generator(must_include1, must_include2, max_len):
    max_length = max_len
    min_length = max_length / 2
    characters = '!@#$%^&*()_+{}:"<>?|'
    low = 4
    high = 365
    low2 = 0
    high2 = 2
    small_ran_number = random.uniform(low2, high2) // 2
    ran_number1 = random.uniform(min_length, max_length)
    ran_number2 = random.uniform(low // ran_number1, high // ran_number1)
    ran_number3 = (ran_number1 // ran_number2)
    ran_letters1 = random.choice(string.ascii_letters)
    ran_characters = random.choice(characters)
    for i in range(int(min_length), int(max_length)):
        passcode = str(ran_number3) + str(ran_number1) + str(ran_characters) + (
                str(ran_letters1) * 10) + must_include1 + must_include2

    l = list(passcode)
    random.shuffle(l)
    result = ''.join(l)
    result = result.replace(".", "")
    if max_length <= 3:
        return print("The length of your password must be greater than 3.")
    if len(result) > max_length:
        L2 = list(result)[:max_length - 2]
        L2.insert(0, must_include1)
        L2.insert(1, must_include2)
        random.shuffle(L2)
        pw = ''.join(L2)
    return pw


def create_random_account_name(min, max, must_include1, must_include2):
    global scale_widget
    return random_pw_generator(must_include1, must_include2, scale_widget.get())


def create_username_pw_combo(title, username_length, pw_length, must_include1, must_include2):
    min = 0
    global scale_widget
    combo = (str(title) +
             " Username: " +
             str(create_random_account_name(min, pw_length, must_include1, must_include2)) +
             " Password: " +
             str(random_pw_generator(must_include1, must_include2, scale_widget.get())))
    return combo


# these are some tests to show what the create_random_account_name function does:
# print(create_username_pw_combo("Google", 0, 11, "&", "#"))
# print(create_username_pw_combo("Facebook", 0, 9, "$", "*"))
# print(create_username_pw_combo("TikTok", 0, 10, "+", "@"))
# print(create_username_pw_combo("Instagram", 0, 10, "^", ":"))


"""USER INTERFACE BELLOW"""
# user interface module is called tkinter and everything bellow
# is how we create buttons, and data entry boxes

from tkinter import *

# frame = LabelFrame(root, text= )
# bellow are the specifications for the the window
# root means like the main window, so root = TK() is saying the User INTERFACE
# is connceted to the module tkinter, the title makes the title when we run the
# program, and the geomtry is creates the size of the window

root = Tk()
root.title("Random Password")
root.geometry("1000x300")

# e = Entry(root) creates a entry box, but the box is not displayed on
# the user interface, until we tell it where it should be placed
# which is in the line: e.grid(row=1, column= 0)
# e.get is how the data that is typed into the box is retrived
# and used by a function, or somewhere in the code

e = Entry(root)
e.grid(row=1, column=0)
e.get()

# another important mention is that everything is located on like a grid
# that used rows and columns, so the type box is in row1 and column 0
# which we specified with the e.grid command. You will see in all of the buttons
# that they have a spcific row and column, which dictates
# where they appear on the screen

# ALL GLOBAL VARIABLES BELLOW: These global variables are used to Store
# the user information.
input_lst = []
LABEL = []
USERNAME = []
PASSWORD = []
SEARCH = ""
LIST_OF_ACCOUNTS = []
COUNT = 0
myLabel1 = Label(root)
myLabel2 = Label(root)
myLabel3 = Label(root)
error = Label(root, text="Needs more account information")
BLANK_SPACE = "                                                           "
Lst_Label = Label(root)
MY_KEYS = []


date_time = datetime.datetime.now()


# there are some global varibes that I put inside the button blocks like:
# global myLabel1
# myLabel1 = Label(root, text = e.get())
# global myLabel2
# myLabel2 = Label(root, text = e.get())

# these are not listed in the list above not for any specific reason,
# mainly because im afraid I might break something if take them
# outside the function. But I think they should work the same if they
# are defined outside of the function because they are global.


# this is the first function which is connected to the button bellow.
# what this function does, is it retrives the data you iput inside of
# e, which is the entry box. Then it dsplays this information in row 2
# column 3 using the mylabel1.grid. Next, it inserts the information
# into the global variable called LABEL which is just an empty list. Notice
# that whenever we clock the label button, it resets the global variable
# using the LABEL.Clear() command. The print is just so we can see
# within the terminal what our global variable is. Whenever you click the button
# the e.delete will clear the entry box, so it is empty again.

def Label_Button():
    global myLabel1
    myLabel1.destroy()
    LABEL.clear()
    # global myLabel1
    myLabel1 = Label(root, text=e.get())
    myLabel1.grid(row=2, column=3)
    # Account_Label = myLabel1.grid(row=2, column=3)
    # input_lst.append(e.get())
    LABEL.insert(0, e.get())
    print(LABEL)
    e.delete(0, END)
    # myButton['state'] = DISABLED

    # this is how the actual button is made. This button is called myButton2
    # which is a variable, that is equal to the Button command. The button
    # command here has all the features inside the parenthesis. Im not
    # really sure how this all works, but the root means its being opened
    # in our main user interface. The text means the letters on the button.
    # padx means the width of the button (you can make it talled with pady)
    # and the command is what is supposed to happen when the button is clicked.
    # one thing to note is that usually when we use a function we need to type it
    # like Label_Button() which includes parenthesis, but when using This
    # button command you do not include the parenthesis for some reason. Another
    # thing that I ran into was that the function needs to be defined before the
    # the button it is connected to, for the button to work.


myButton = Button(root, text="Account Name", padx=25, command=Label_Button)
myButton.grid(row=2, column=0)


# here is the next button for the username. It pretty much has all the same
# features as the label button. Once we get a single button working, the rest
# are just pretty much copies assigned to different functions.


def Username_Button():
    global myLabel2
    USERNAME.clear()
    myLabel2.destroy()
    # myLabel2 = Label(root, text = "")
    myLabel2 = Label(root, text=e.get())
    myLabel2.grid(row=3, column=3)
    # Account_Label = myLabel1.grid(row=3, column=3)
    # input_lst.append(e.get())
    USERNAME.insert(1, e.get())
    print(USERNAME)
    # myButton2['state'] = DISABLED
    e.delete(0, END)


myButton2 = Button(root, text="Username", padx=25, command=Username_Button)
myButton2.grid(row=3, column=0)


# Notice that the row is growing. That is how we put the buttons are bellow one another

# The password button is slightly different from the previous two,
# Because it does not take any information from the data that
# is entered in the e = entry box. Rather, when we hit the Password_Button
# it runs the random_pw_generator function with specified inputs bellow.
# The variables that are s, A, and B are used to pick random input variables
# for the function, just to add another layer of randomness. This is why the
# the password is a different length whenever we generate one (or most of the time).
#
# this line here:
# low2 = 18; high2 = 26
# s = random.uniform(low2, high2) // 2
# chooses some random number between 9 and 13, and the variable s, is then used
# for the Max lenght input. Notice that I set the min to 0. This is something
# that is curently not being used, but will probably be useful when creating
# the slider.


def Password_Button():
    global myLabel3
    myLabel3.destroy()
    global COUNT
    PASSWORD.clear()
    characters = '!@#$%^&*()_+{}:"<>?|'
    Upper_Case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low2 = 18
    high2 = 26
    s = random.uniform(low2, high2) // 2
    A = random.choice(characters)
    B = random.choice(Upper_Case)
    global scale_widget
    # read the selected value from the slider and pass it to the passwd generator
    Code = str(random_pw_generator(str(A), str(B), scale_widget.get()))
    PASSWORD.insert(0, Code)
    myLabel3 = Label(root, text=Code)
    if COUNT < 1:
        myDelete()
        COUNT = 1 + COUNT
        myLabel3.grid(row=4, column=3)

        # PASSWORD.insert(0, Code)
    else:
        myDelete()
        # myLabel3.destroy()
        # myLabel3 = Label(root, text = Code)
        COUNT = 1 + COUNT
        print("yay")
        # Code = str(random_pw_generator(0, int(s) , str(A), str(B)))

        # myLabel3.grid(row=4, column=3)
        # PASSWORD.insert(0, Code)
        print(PASSWORD)
    # PASSWORD.insert(0, Code)
    myLabel3.grid(row=4, column=3)
    # myButton3['state'] = DISABLED
    print(PASSWORD)
    e.delete(0, END)


myButton3 = Button(root, text="Password", padx=25, command=Password_Button)
myButton3.grid(row=4, column=0)

scale_widget = Scale(root, orient="horizontal", resolution=1,
                     from_=10, to=20)
label_1 = Label(root, text="Set Password Length")
label_1.grid(row=5, column=0)
scale_widget.grid(row=6, column=0)


# the save button is how we create a history. function will be useful
# in order to make some kind of download capability (Daniela).
# First a everytime we call the Save_Button function we create an
# empty dictionary called new_dict. That is important beceause that means
# that every time we click the save button, it deletes the old item in
# the dictionary by setting the dictionary to empty.
#
# This next part is the hard/ weird part.
#
# next the function sets the key of new_dict to the 0th item of LABEL. LABEL
# is the global variable that is recorded everytime we hit the LABEL button.
# Then, LABEL is converted into a string. This string is now the KEY
# of new_dict. Next, the = sign is what creates the value of the dictionary.
# the value in this case is:
#  "Username: " + str(USERNAME[0]) + "    Password: " + str(PASSWORD[0])
# This is just CONVERTING the global varibles USERNAME and PASSWORD into
# strings, then all of these strings are combined using the " + " symbol.
#
# The final part of the save button/function is to append this dictionary
# into the global variable LIST_OF_ACCOUNTS. so this means that that the
# items inside LIST_OF_ACCOUNTS are all long strings like:
# [{'TikTok': 'Username: paulfmusic    Password: 4HM13M3*359H'}]
# the square brackets on the outside show that we have a list, and the first
# item of the list is:
# {'TikTok': 'Username: paulfmusic    Password: 4HM13M3*359H'}
# The reason why we can keep a running list of all of our user/ password
# label combinations, is because each time we hit the save button
# we just append a new item onto the global list LIST_OF_ACCOUNTS.


def Save_Button():
    if len(LIST_OF_ACCOUNTS) > 12:
        Max_Out_Lst = Label(root, text="Max Number of Accounts Reached")
        Max_Out_Lst.grid(row=1, column=3)
        return print("Max Number of Accounts Reached")
        Max_Out_List = Label(row=1, )
    global error
    # global new_dict
    if ((BLANK_SPACE in LABEL) or (BLANK_SPACE in USERNAME) or (BLANK_SPACE == PASSWORD)
            or (len(LABEL) == 0) or (len(USERNAME) == 0) or (len(PASSWORD) == 0)):
        error = Label(root, text="Needs more account information")
        error.grid(row=1, column=3)
        e.delete(0, END)
        return error
    else:
        new_dict = {}
        new_dict[str(LABEL[0])] = str(date_time.strftime("%A, %B, %d, %Y")) + "    Username: " + str(
            USERNAME[0]) + "    Password:   " + str(PASSWORD[0] + "   ")
        LIST_OF_ACCOUNTS.append(new_dict)
        print(new_dict)
        print(LIST_OF_ACCOUNTS)
        e.delete(0, END)
        COUNT = 0
    # Clear_Button()
    # print(str(LABEL[0]))
    print("woop")
    print(str(USERNAME[0]))
    MY_KEYS.append(LABEL[0])
    # print(str(PASSWORD[0]))
    myButton3['state'] = NORMAL
    myButton2['state'] = NORMAL
    myButton['state'] = NORMAL


myButton4 = Button(root, text="Save", padx=25, command=Save_Button)
myButton4.grid(row=1, column=1)


# This Cleaer button is not working yet. It was working before for certain
# inputs, but I will try to fix this button. This button should just
# just clear all the information on the screen, pretty much
# reseting all the data on the screen.

def Clear_Button1():
    myLabel1.destroy()
    error.destroy()
    # myButton['state'] = NORMAL


def myDelete():
    myLabel3.grid_forget()


myButton5 = Button(root, text="Clear", padx=25, command=Clear_Button1)
myButton5.grid(row=2, column=1)


def Clear_Button2():
    myLabel2.destroy()
    error.destroy()
    # myButton2['state'] = NORMAL


myButton5 = Button(root, text="Clear", padx=25, command=Clear_Button2)
myButton5.grid(row=3, column=1)


def Clear_Button3():
    myLabel3.destroy()
    error.destroy()
    # myButton3['state'] = NORMAL


myButton5 = Button(root, text="Clear", padx=25, command=Clear_Button3)
myButton5.grid(row=4, column=1)


def Clear_Button():
    Clear_Button1()
    Clear_Button2()
    Clear_Button3()


myButton5 = Button(root, text="Clear All", padx=25, command=Clear_Button)
myButton5.grid(row=10, column=0)

# Bellow is the search function in progress. I might finish this blocks
# but will put this on the side until I can figure out how to just display
# all of the label,username,password combos on the screen.

test_lst = ["{'Google': 'Monday, August, 03, 2020    Username: fentresspaul@gmail.com    Password:   TT1T85^3T0P   '}",
            "ig", "tiktok"]
test_lst2 = ["{'Google': 'Monday, August, 03, 2020    Username: fentresspaul@gmail.com    Password:   TT1T85^3T0P   '}"]


def split(word):
    return [char for char in word]


def display_my_lsts_func():
    Clear_Button()
    myButton['state'] = DISABLED
    myButton2['state'] = DISABLED
    myButton3['state'] = DISABLED
    global Display_Lst
    Display_Lst = []
    for i in range(len(LIST_OF_ACCOUNTS)):
        Lst_Label = Label(root, text=LIST_OF_ACCOUNTS[i])
        Display_Lst.append(Lst_Label)
        Lst_Label.grid(row=i + 2, column=3)
        print(Lst_Label)


myButton7 = Button(root, text="Show My Accounts", padx=25, command=display_my_lsts_func)
myButton7.grid(row=11, column=0)


def hide_my_lsts_func():
    myButton['state'] = NORMAL
    myButton2['state'] = NORMAL
    myButton3['state'] = NORMAL
    global Display_Lst
    for i in range(len(LIST_OF_ACCOUNTS)):
        print("entering for loop")
        Lst_Label = Display_Lst[i]
        Lst_Label.destroy()


myButton7 = Button(root, text="Hide My Accounts", padx=25, command=hide_my_lsts_func)
myButton7.grid(row=12, column=0)

# def myDelete():
#     myLabel3.grid_forget()
#     myButton3['state'] = NORMAL

import csv 
def save_csvfile():
    csv_column = MY_KEYS
    csv_column = list(dict.fromkeys(csv_column))
    new_list = []
    for x in range(0,len(LIST_OF_ACCOUNTS)):
        new_list.append(LIST_OF_ACCOUNTS[x])
        print(LIST_OF_ACCOUNTS[x])
    file = open('userhistory.csv','w+', newline = '')
    with file:
            write = csv.DictWriter(file, fieldnames = csv_column)
            write.writeheader()
            write.writerows(new_list)


#
myButton9 = Button(root, text="Save CSV File", padx=25, command=save_csvfile)
myButton9.grid(row=13, column=0)

root.mainloop()

# the root.mainloop ends the user interface. So everything that we want to to
# within the user interface must be above this line, and bellow
# the root = TK further up
