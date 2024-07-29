from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("230x450")
root.title("Calculator By Taha Qamar")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Define the button layout
button_layout = [
    ["9", "8", "7", "*"],
    ["6", "5", "4", "-"],
    ["3", "2", "1", "+"],
    ["0", "/", "C", "="],
    [".", "^", "(", ")"]
]
# Define button color
button_color = "powder blue"

# Loop through the button layout and create buttons
for row in button_layout:
    f = Frame(root, bg="gray")
    for btn_text in row:
        b = Button(f, text=btn_text, padx=5, pady=5, font="lucida 20 bold",bg=button_color, fg="black")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    f.pack()



root.mainloop()
