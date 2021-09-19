# Password-Generator

The program is used to create account information with random passwords. When you click the save button, it will save all the information on the screen to a running list. You can show accounts, and hide accounts with the respective buttons. The search button will search through your accounts to find accounts with the key word. The final step would be to hit the save CSV button, which would update your csv user history file.
To run the program use the terminal. In order to utilize the SAVE_CSV function, you must already have a CSV file in the same folder that the program exists called: “userhistory.csv”. After you hit the save csv file, to see if it has worked, go to your finder, and open the “userhistory.csv” file. This should have the updated version of your accounts.
In order to run the tests, run the command: python3 -m unittest Final_Test.py which is in its own file.

Features:
     1. Random Password Generator
     2. Search Function
     3. Save to CSV file function
Complexity:
 ○ How did your features contribute to complexity?
The functions we used are difficult, because we had to create them to work obviously, but then had to also make sure they worked within the framework of the user interface. The user interface created many obstacles to work around, so we had to change our functions in to fit the requirements of the Tkinter module.
     
     ● We used list comprehension, dictionaries, lists, and classes within the program. We used multiple modules like Tkinter, datetime, random, and csv, which were new to all of us.
     ● We made use of functional programming. We made multiple helper functions that were called inside of other functions.
Lists & Script Variables" 
     ● Use lists and script variables in your project.

The lists we used include the LIST_OF_ACCOUNTS which was a global list used to save the information, and to display account information on the screen. The second list we use is the passcode list, which saves random characters into a list and then shuffles all the list items, and returns a new list. That list is then joined together, which creates the random passwords. Another list we used was the display_lst, which creats a new version of LIST_OF_ACCOUNTS in order to remove items from the screen or display them. We used global lists to keep track of our current username, account name, and passwords. We used script variables in our Button functions in order to keep track of the input in the text bar for example USERNAME = e.get() is the command we used to store the text inside the text bar, as our username. Another script variable we used were the multiple random characters inside the random password generator function.
Function Table
Each row will describe the functionality of one custom block/function, with the relevant information placed in the relevant columns (as defined above). You must include a separate row for EVERY custom block/function you create
        Block / Function Name
Domain (inputs)
Range (outputs)
Behavior (role in the context of the project)
random_pw_generator
must include1, must include 2
A random password that contains the specified inputs
This function is connected to another function, which we can edit how long we would like our random password to be using the visual slider bar.
search_func3
Keyword, lst_of_dictionarie s
The saved accounts that contain the keyword.
This function is one of multiple used in order to search through the database of accounts, and then display the accounts that contain the search word.
    
        save_csv
None
Creates a table of accounts inside the csv file that display all of the account information.
Random password
Updates the information in a csv file that is saved within the same folder as the program. This way the user could print out this file, to maximize their password security.
      Label_Button
None
Data entered into text box.
Saves the information from the text box, then displays it on the UI when the button is pressed.
      Username_Button
None
Data entered into text box.
Saves the information from the text box, then displays it on the UI when the button is pressed.
    myDelete
None
Clears password
Updates ui so the random password is gone. This is a helper function
  Helper function to display random password on UI
    Save_Button
None
List of dictionaries
Appends a dictionary of account information onto global list which is used throughout the program
    Clear_Button
None
Takes items off screen in UI
Used in order to remove items from the screen. We often have to clear the item on the screen before updating a new one, so they don’t overlap.
    split
Word
List of characters
Helper function for search functions. Splits a word into a list of characters.
       keep_search
keyword, lst_of_dictionarie s
A new list
This is a helper function that utilizes the search_func3. Using list comprehension, the keep search func keeps all the items in the list that contain the search word.
          Password_Button None
   
     Search results
 Displays search results on UI
List of dictionaries
 Displays all accounts on UI
List of dictionaries
 Hides all accounts from UI
  search_func_Button None
display_my_lsts_func None
hide_my_lsts_func None
Extra Credit (optional)
Please use this space to discuss any EC implementations. Extra credit opportunities:
Use some external library or features of Python that we did not explicitly
teach
Use of the modules including Tkinter, random, string, CSV, and Datetime. Creating the user interface was a significant part of the project, but seemed important bring the ideas together. Tkinter had many specific features we had to edit our functions to work with.
    
