import pandas as pd 

def create_message(template, *arg):
    message = template.format(*arg)
    print (message)
    return message

input_spreadsheet = pd.read_csv("./send_list_1.csv", encoding ="cp1252")
input_tuples = input_spreadsheet.to_records(index=False)
input_list = list(input_tuples)

something = "This message contain {} and {} and {}"

# for i,j in enumerate (input_list):
#     message = create_message(something, *input_list[i])
