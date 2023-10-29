import tkinter as tk

def click_button(char):
    current_text = result_display.get()
    if current_text == "Error":
        result_display.set("")

    if char == 'Ans':
        try:
            result = eval(current_text)
            result_display.set(result)
        except Exception:
            result_display.set("Error")
    elif char == 'C':
        result_display.set("")
    else:
        result_display.set(current_text + str(char))

app = tk.Tk()
app.title("Calculator")

result_display = tk.StringVar()
result_display.set("")
display_label = tk.Label(app, textvariable=result_display, font=('Arial', 20))
display_label.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', 'Ans', '+'
]

row, col = 1, 0
for button in buttons:
    tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda char=button: click_button(char)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
app.mainloop()
