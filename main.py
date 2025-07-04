from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton
from PyQt5.uic import loadUi
from sys import argv
from random import choice

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        # Load the UI
        loadUi("interface.ui", self)

        # Define our variables
        self.text_edit = self.findChild(QTextEdit, "textEdit")
        code_PushButton = self.findChild(QPushButton, "code_PushButton")
        decode_PushButton = self.findChild(QPushButton, "decode_PushButton")
        
        # Add a fucntions to all buttons
        code_PushButton.clicked.connect(self.code_it)
        decode_PushButton.clicked.connect(self.decode_it)

        # Show the main window
        self.show()

    def code_it(self):
        # Grab the text
        text = self.text_edit.toPlainText()
        # Check it is plain text or code?
        permission = self.give_permission_toCode(text)
        # Check permission is true( true:plain text, False:code )
        if permission:
            # Convert into the code
            code = self.code(text=text)
            # Set the text
            self.text_edit.setPlainText(code)

    def decode_it(self):
        # Grab the text
        text = self.text_edit.toPlainText()
        # Convert into the decode
        decode = self.decode(text=text)
        # Set the text
        self.text_edit.setPlainText(decode)
    
    def code(self, text):
        # In, new text the text will store with out any new line, spaces and tab
        new_text = ""

        # The tab mean 4 blank spaces
        tab = "    "

        # Character replace with new line (Which will be replace with the \n)
        character_for_newLine = [" *.* "," /%? "," $*! "]
        # Character replace with tab (Which will be replace with the \t)
        character_for_tab = [" !@$ ",' \*$ '," `]{ "]
        # Character replace with tab (Which will be replace with the \t)
        character_for_blankSpace = [" @!$ ", ' !*% ', " &@| "]

        # Replace all tab with random word 
        text = text.replace(tab, choice(character_for_tab))

        # Loop for itreate all text
        for character in text:
            if character == "\n":
                # Check the character is new line and append the special word from character_for_newLine randomly.
                new_text += choice(character_for_newLine)
            elif character == " ":
                # Check the character is blank space and append the special word from character_for_blankSpace randomly.
                new_text += choice(character_for_blankSpace)
            else:
                # Check the character is simple word.
                new_text += character
                

        # Seprate the words in the new_text as list by blank space
        words = new_text.split(" ")

        # Create the list for store the rearranged word
        rearranged = []

        # Loop for arrange the words
        for word in words:
            # Check that word is new line.
            if character_for_newLine[0][1:-1] == word or character_for_newLine[1][1:-1] == word or character_for_newLine[2][1:-1] == word:
                    # Put into the rearranged list as it is.
                    rearranged.append(word)

            # Check that word is tab.
            elif character_for_tab[0][1:-1] == word or character_for_tab[1][1:-1] == word or character_for_tab[2][1:-1] == word :
                    # Put into the rearranged list as it is.
                    rearranged.append(word)

            # Check that word is blank space.
            elif character_for_blankSpace[0][1:-1] == word or character_for_blankSpace[1][1:-1] == word or character_for_blankSpace[2][1:-1] == word:
                    # Put into the rearranged list as it is.
                    rearranged.append(word)
            else:
                #  Check the lenght of word is greater tha 2 or not
                if (len(word) >= 2):
                    # Create the new variabele that will store the rearranged word 
                    new_word = word[-1] + word[1:-1] + word[0]
                    # Put into the rearranged list
                    rearranged.append("".join(new_word))

                else:
                    # Create the temporary list
                    li =[]
                    # Itreate the word
                    for char in word:
                        # put the character in the list.
                        li.append(char) 
                    
                    # Sort left to right(reverse)
                    li.sort()
                    
                    # Create the new variabele that will store the reversed word
                    new_word = "".join(li)

                    # Put into the rearranged list
                    rearranged.append(new_word)

        # Convert the rearanged in string!
        code = "".join(rearranged)

        # Return the value
        return code

    def decode(self, text):
        # tab means (4 blank spaces)
        tab = "    "

        # Character replace for new line 
        character_for_newLine = ["*.*", "/%?", "$*!"]
        # Character replace for tab 
        character_for_tab = ["!@$", '\*$', "`]{"]
        # Character replace for blank space 
        character_for_blankSpace = ["@!$", '!*%', "&@|"]

        # if replace special chracter of character_for_blankSpace with " "
        text = text.replace(character_for_blankSpace[0], " ")
        text = text.replace(character_for_blankSpace[1], " ")
        text = text.replace(character_for_blankSpace[2], " ")

        # if replace special chracter of character_for_blankSpace with tab
        text = text.replace(character_for_tab[0], tab)
        text = text.replace(character_for_tab[1], tab)
        text = text.replace(character_for_tab[2], tab)

        # if replace special chracter of character_for_blankSpace with new line
        text = text.replace(character_for_newLine[0], " \n ")
        text = text.replace(character_for_newLine[1], " \n ")
        text = text.replace(character_for_newLine[2], " \n ")

        # Seprate word in the new_text as list
        words = text.split(" ")

        # Create the list for store the rearranged word
        rearranged = []

        # Loop for rearrange words
        for word in words:
            # Check that word is in any list(mean to say speacial character)
            if word in character_for_newLine: 
                    # Put into the rearranged list
                    rearranged.append("\n")
            elif word in character_for_tab :
                    # Put into the rearranged list
                    rearranged.append(tab)
            elif word in character_for_blankSpace:
                    # Put into the rearranged list
                    rearranged.append(' ')
            else:
                #  Check the lenght of word is greater tha 2 or not
                if (len(word) >= 2):
                # Create the new variabele to store re arranged word 
                    new_word = word[-1] + word[1:-1] + word[0]

                # Put into the rearranged list
                    rearranged.append("".join(new_word))

                else:
                    # Create the temporary list
                    li =[]
                    # Itreate the word and put in the list
                    for char in word:
                        li.append(char) 
                    
                    # Sort left to right(reverse)
                    li.sort()

                    # Put into the rearranged list
                    rearranged.append("".join(li))

        # Convert the rearanged in string and solve problem with dirty way!
        decode = " ".join(rearranged).replace(" \n ", "\n")
        
        # Return the decode
        return decode
    
    def give_permission_toCode(self, text:str):
        # For keep track the postion
        permistion = True

        # Character replaced with new line 
        character_for_newLine = ["*.*", "/%?", "$*!"]
        # Character replaced with tab 
        character_for_tab = ["!@$", '\*$', "`]{"]
        # Character replaced with blank space 
        character_for_blankSpace = ["@!$", '!*%', "&@|"]

        # Check the speacial character if it is in the text(Its mean text is code)
        if character_for_newLine[0] in text or character_for_newLine[1] in text or character_for_newLine[2] in text:
            permistion = False
        if character_for_tab[0] in text or character_for_tab[1] in text or character_for_tab[2] in text:
            permistion = False
        if character_for_blankSpace[0] in text or character_for_blankSpace[1] in text or character_for_blankSpace[2] in text:
            permistion = False
        # If permisstion is True than some thing can be happem
        return permistion


if __name__ == "__main__":
    # Create the application
    app = QApplication(argv)
    # Create the Ui
    ui = Ui_MainWindow()
    # Execute the application
    app.exec_()