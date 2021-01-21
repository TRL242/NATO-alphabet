import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#pull file call it data
data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

def generate_phonetic():
    word = input("Hi, please type what you need to see the phonetic of: \n").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError or NameError:
        print("Only use letters.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

