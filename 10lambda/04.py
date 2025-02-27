from tkinter import Button, mainloop

button = Button(
    text='This is a button',
    command=lambda: print('being clicked')
)

button.pack()
mainloop()