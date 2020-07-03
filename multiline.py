from parse_text import create_message
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.geometry("400x240")

def get_template():
    template=textExample.get("1.0","end")
    print(template)

    input_spreadsheet = pd.read_csv("./send_list_1.csv", encoding ="cp1252")
    input_tuples = input_spreadsheet.to_records(index=False)
    input_list = list(input_tuples)

    for i,j in enumerate (input_list):
        message = create_message(template, *input_list[i])


textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=get_template)

btnRead.pack()

root.mainloop()