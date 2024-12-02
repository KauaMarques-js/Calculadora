import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.equation = ""
        self.display_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        display = tk.Entry(self.root, textvariable=self.display_text, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        display.grid(row=0, column=0, columnspan=5)  # Atualizado para 5 colunas

        buttons = [
            '7', '8', '9', '/', 'CE',
            '4', '5', '6', '*', 'C',
            '1', '2', '3', '-', '<=',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == 'CE':
                action = self.clear_all
            elif button == 'C':
                action = self.clear_entry
            elif button == '<=':
                action = self.backspace
            else:
                action = lambda x=button: self.on_button_click(x)
            
            b = tk.Button(self.root, text=button, padx=20, pady=20, font=("Arial", 18), command=action)
            b.grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.equation))
                self.display_text.set(result)
                self.equation = result
            except Exception as e:
                self.display_text.set("Erro")
                self.equation = ""
        else:
            self.equation += str(char)
            self.display_text.set(self.equation)

    def clear_all(self):
        self.equation = ""
        self.display_text.set("")

    def clear_entry(self):
        self.equation = ""
        self.display_text.set("")

    def backspace(self):
        self.equation = self.equation[:-1]
        self.display_text.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
