import string as s
import random
import tkinter as tk
from typing import Text

class PasswordGenerator():
    def __init__(self, 
                min_length  : int   = 0, 
                max_length  : int   = 8, 
                letters     : bool  = True,
                digits      : bool  = True, 
                punctuation : bool  = True
            ):
        
        self.min_length     = min_length
        self.max_length     = max_length

        self.letters        =  s.ascii_letters
        self.digits         =  s.digits
        self.punctuation    =  s.punctuation

        self.chars          = self.generate_chars(letters, digits, punctuation)
        self.password       = self.generate_password()
    
    def generate_chars(self, letters, digits, punctuation):
        chars = ""

        if letters:
            chars += self.letters
        
        if digits:
            chars += self.digits
        
        if punctuation:
            chars += self.punctuation
        
        return " ".join(chars).split(" ")

    def generate_password(self):
        passwd = ""
        
        for char in range(self.min_length, self.max_length):
            _char = random.choice(self.chars)
            passwd += str(_char)

        return passwd

class Window():
    def __init__(self) -> None:
        root                = tk.Tk()
        root                .configure(bg="#fff")

        root                .title("Password Generator")
        root                .geometry("240x110")
        root                .resizable(False, False)
        
        root                .grid_columnconfigure(0, weight=1)

        self.letters        = tk.BooleanVar(value=True)
        self.digits         = tk.BooleanVar(value=False)
        self.punctuation    = tk.BooleanVar(value=False)
        
        self._letters       = tk.Checkbutton(root,text="Letters", variable=self.letters,bg="#fff")
        self._digits        = tk.Checkbutton(root, text="Digits", variable=self.digits,bg="#fff")
        self._punctuation   = tk.Checkbutton(root, text="Punctuation", variable=self.punctuation,bg="#fff")       
        
        self.placeHolder    = tk.StringVar(root, value="8")
        self.max_length     = tk.Entry(root, textvariable=self.placeHolder, width=5, justify="center")
        self.generate_btn   = tk.Button(root, text="Generate Password", command=lambda: self.generate_password(), relief="flat", bg="#222222", fg="#fff")

        self.password       = tk.StringVar(root, value="")
        self._password      = tk.Entry(root, textvariable=self.password)
        
        self._letters       .grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
        self._digits        .grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
        self._punctuation   .grid(row=0, column=2, padx=2, pady=2, sticky="nsew")
        
        self.max_length     .grid(row=1, padx=2, pady=2, sticky="nsew", columnspan=3)
        self.generate_btn   .grid(row=2, padx=2, pady=2, sticky="nsew", columnspan=3)
        self._password      .grid(row=3, padx=2, pady=2, sticky="nsew", columnspan=3)

        self                .mainLoop(root)

    def generate_password(self):
        self.password.set("asd")
        password = PasswordGenerator(max_length=int(self.max_length.get()), letters=self.letters.get(), digits=self.digits.get(), punctuation=self.punctuation.get()).password
        self.password.set(password)
    
    def mainLoop(self, root):
        root.mainloop()

if __name__ == "__main__":
    Window()
