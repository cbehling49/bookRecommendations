"""
Project 4 - Book GUI
Cody Behling
CS-1410-602

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating.
I will receive a zero on this project if I am found in violation of this policy.
"""

import bookRecs
from breezypythongui import EasyFrame


class BookGUI(EasyFrame):
    def __init__(self):
        # main window
        EasyFrame.__init__(self, title="Main Window", background="powder blue", width=300, height=100)
        self.addButton(text="Friends", row=0, column=0, command=self.friends)
        self.addButton(text="Recommend", row=0, column=1, command=self.recommend)
        self.addButton(text="Report", row=0, column=2, command=self.report)

    def friends(self):
        # prompter box from friends button
        pbReaderName = self.prompterBox(title="Friends", promptString="Enter Reader Name:")
        if pbReaderName not in bookRecs.ratings:
            self.messageBox(title="ERROR", message="No such reader.")
            return
        else:
            friendsList = f"{bookRecs.friends(pbReaderName)[0]}\n{bookRecs.friends(pbReaderName)[1]}"
            self.messageBox(title=f"Friends of {pbReaderName.capitalize()}", message=friendsList)

    def recommend(self):
        # prompter box from friends button
        pbReaderName = self.prompterBox(title="Recommendations", promptString="Enter Reader Name:")
        if pbReaderName not in bookRecs.ratings:
            self.messageBox(title="ERROR", message="No such reader.")
            return
        else:
            booksList = bookRecs.recommend(pbReaderName)
            output = ''
            for book in booksList:
                output += f'{book}\n'
            self.messageBox(title=f"Recommendations for {pbReaderName.capitalize()}", message=output, width=100, height=25)

    def report(self):
        reportList = bookRecs.full_report()
        self.messageBox(title="Report", message=reportList, width=100, height=25)


def main():
    BookGUI().mainloop()


if __name__ == "__main__":
    main()
