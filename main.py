from random_word_generator import pick_random_word
import string

def string_input_converter(input_char1,selected_word):

    str=string.ascii_letters
    
    # getting index of input_char in str
    index=str.find(input_char1)

    #If input_char and selected_word is same
    if input_char1 in selected_word: 
        return input_char1
    
    #If input_char and selected_word are different 
    else:
        #input_char is lowerCase and selected_word is UpperCase
        if (index<26 and (str[index] in selected_word)):
            return str[index+26]
        
        #input_char is UpperCase and selected_word is LowerCase
        else:
            (index>26 and (str[index] in selected_word))
            return str[index-26]


# Function to change current word state depneding on the input from user
def change_current_word_state(selected_word, input_char, current_word_state):
    modified_word_state=""

    for i in range(len(selected_word)):
        if current_word_state[i]=='_' and selected_word[i]==input_char:
            modified_word_state+=selected_word[i]
        else:
            modified_word_state+=current_word_state[i]
        
    return modified_word_state

#If the Input character is in "selected_word", this function will update "current_word_state" or either it will decrease "attempts_remaining"
def input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining):

    # if the 'input_char' is in 'Selected_word', change 'current_word_state'

    if input_char in selected_word:
        current_word_state=change_current_word_state(selected_word, input_char, current_word_state)
    
    # else if the 'input_char' is not in 'Selected_word', decrease 'attempts_remaining'
    else:
        attempts_remaining-=1                       
    
    return current_word_state, attempts_remaining


# Function to print current state of the word
def print_current_state(current_word_state, attempts_remaining): #this function will print current state of the word, i.e. word guessed so far by user and attempts left
    print("Current word state:",end=" ")

    for i in current_word_state:
        print(i,end=" ")
    print("\t Attempts Remaining:{}".format(attempts_remaining))

#function to check status of game, i.e. 
def check_game_status(selected_word, current_word_state, attempts_remaining):
    if attempts_remaining<=0:
        print("Sorry :(\nYOU LOST: try again!")
        print("The word was: {}".format(selected_word))
        return False
    if selected_word==current_word_state:
        print("Congratulations :)\nYOU WON")
        return False
    return True


def play_game(attempt=5):
    # random word is selectedt
    selected_word=pick_random_word() 
    
    # It will show present state of word
    current_word_state="" # string to store current word input from user

    #Hiding Consonants 
    for i in selected_word:
        if i==" " or i=="a" or i=='e' or i=='i' or i=='o' or i=='u' or i=="A" or i=='E' or i=='I' or i=='O' or i=='U' or i=="\n":
            current_word_state+=i
        else:
            current_word_state+='_'

    attempts_remaining=attempt  # Initialising attempts

    print_current_state(current_word_state,attempts_remaining)

    while True:
        input_char1=input("Guess the character: ")
        print(" ")

        #This function will change case of input_char depending on Selected_word
        input_char=string_input_converter(input_char1,selected_word)

        current_word_state,attempts_remaining=input_char_in_word(selected_word,input_char,current_word_state,attempts_remaining)
        print_current_state(current_word_state, attempts_remaining)
        game_end_checker=check_game_status(selected_word, current_word_state, attempts_remaining)

        if game_end_checker==False:
            break


if __name__=="__main__":
    play_game()
    