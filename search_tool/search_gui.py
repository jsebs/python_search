import customtkinter as ctk
import tkinter as tk


# basic style params
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


# App class to define GUI elements and grids
class AppGui(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Search Tool")
        self.geometry("600x700")
        self.minsize(500, 600)

        # label for title
        self.appTitle = ctk.CTkLabel(self, text="Search Tool", font=("Roboto", 16))
        self.appTitle.grid(row=0, column=0,
                           columnspan=6, padx=20,
                           pady=(20, 0))

        # label to provide an overview of app and instructions
        self.appDesc = ctk.CTkLabel(self,
                                    text="This app is meant to speed up the mind-numbing task of \n"
                                    "searching through various files for a specific name/email/city/string.\n\n"
                                    "Currently supported filetypes are: .csv, .xls, .xlsx, and .txt\n\n"
                                    "To use, click the 'Browse' button and navigate to the directory\n"
                                    "containing the files you wish to search, enter the string you're \n"
                                    "looking for in the box below the browse section, and hit search.",
                                    font=("Roboto", 14))
        self.appDesc.grid(row=1, column=0, columnspan=6,
                          padx=20, pady=20)

        # browse button + field to display chosen directory
        self.browseBtn = ctk.CTkButton(self, text="Browse")
        self.browseBtn.grid(row=2, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        self.browseEntry = ctk.CTkEntry(self, placeholder_text="Source directory")
        self.browseEntry.grid(row=2, column=1,
                              columnspan=5, padx=20,
                              pady=50, sticky="ew")

        # field to enter search string + search button
        self.searchEntry = ctk.CTkEntry(self, border_color="#FFFFFF", placeholder_text="Enter search string here")
        self.searchEntry.grid(row=3, column=0, columnspan=5,
                              padx=150, pady=30,
                              sticky="ew")

        self.searchBtn = ctk.CTkButton(self, text="Search")
        self.searchBtn.grid(row=4, column=0, columnspan=5,
                            padx=150,
                            sticky="ew")

        # textbox to return results of search
        self.textbox = ctk.CTkTextbox(self)
        self.textbox.grid(row=5, column=0,
                          columnspan=6, padx=20,
                          pady=20, sticky="nsew")

        # adjust column weights for centering
        for col in range(6):
            self.grid_columnconfigure(col, weight=1)


if __name__ == "__main__":
    app = AppGui()
    app.mainloop()
