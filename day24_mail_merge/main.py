#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# python100days\day24_mail_merge\Input\Letters

with open('./Input/Letters/starting_letter.txt', 'r') as in_file:
    starting_letter = in_file.read()

with open('./Input/Names/invited_names.txt', 'r') as in_file:
    for name in in_file:
        stripped_name = name.strip()
        finished_letter = starting_letter.replace('[name]', stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as out_file:
            out_file.write(finished_letter)

