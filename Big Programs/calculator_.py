import tkinter as tk
from tkinter import ttk, messagebox

class DawillyGeneCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("DawillyGene Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.setup_ui()
        self.bind_keyboard()

    def setup_ui(self):
        # Create display field
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            font=('Arial', 24),
            justify='right',
            state='readonly'
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('⌫', 5, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            btn = ttk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def bind_keyboard(self):
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<BackSpace>', lambda e: self.backspace())
        self.root.bind('<Escape>', lambda e: self.clear())
        for char in '0123456789+-*/.()':
            self.root.bind(char, lambda e, c=char: self.add_to_display(c))

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        else:
            self.add_to_display(char)

    def add_to_display(self, char):
        current = self.display_var.get()
        self.display_var.set(current + char)

    def clear(self):
        self.display_var.set('')

    def backspace(self):
        current = self.display_var.get()
        self.display_var.set(current[:-1])

    def calculate(self):
        try:
            expression = self.display_var.get()
            if not expression:
                return
            
            # Replace × with * and ÷ with / for eval
            expression = expression.replace('×', '*').replace('÷', '/')
            
            # Evaluate expression
            result = eval(expression)
            
            # Handle division by zero
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.display_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")
            self.clear()

if __name__ == '__main__':
    root = tk.Tk()
    app = DawillyGeneCalculator(root)
    root.mainloop()