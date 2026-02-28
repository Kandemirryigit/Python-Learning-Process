PLACEHOLDER= "[name]"






with open("C:/Users/CASPER/Desktop/python_projects/project34/Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()



with open("C:/Users/CASPER/Desktop/python_projects/project34/Input/Letters/starting_letter.docx") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"C:/Users/CASPER/Desktop/python_projects/project34/Output/ReadyToSend/letter_for_{stripped_name}.docx","w") as completed_letter:
            completed_letter.write(new_letter)

       
       