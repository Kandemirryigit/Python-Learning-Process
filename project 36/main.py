import pandas

data=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/project 36/nato_phonetic_alphabet.csv")

phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}


try:
    word=input("Enter a word: ").upper()
    output_list=[phonetic_dict[letter] for letter in word]
    print(output_list)
except KeyError:
      print("you can just use english alphabet.No numbers and no another alphabet")
