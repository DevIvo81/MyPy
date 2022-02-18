import tkinter as tk


def add_two_numbers():
    first_number = int(txt_entry_first_number.get())
    second_number = int(txt_entry_second_number.get())
    result_var.set(first_number + second_number)


def substrackt_two_numbers():
    pass



root = tk.Tk()
root.title('Algebra Simple Calc')
root.geometry('700x500')


lbl_first_number = tk.Label(root, text='Prvi broj')
lbl_first_number.grid(row=0, column=0, padx=5, pady=5)
txt_entry_first_number = tk.Entry(root)
txt_entry_first_number.grid(row=0, column=1, padx=5, pady=5)

lbl_second_number = tk.Label(root, text='Drugi broj')
lbl_second_number.grid(row=1, column=0, padx=5, pady=5)
txt_entry_second_number = tk.Entry(root)
txt_entry_second_number.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text='+', command=add_two_numbers)
btn_add.grid(row=2, column=0, padx=5, pady=5)

btn_substract = tk.Button(root, text='-', command=substrackt_two_numbers)
btn_substract.grid(row=2, column=1, padx=5, pady=5,)

result_var = tk.IntVar()
result_var.set(0)

lbl_result = tk.Label(root, textvariable=result_var)
lbl_result.grid(row=3, column=0, padx=5, pady=5)


root.mainloop()
