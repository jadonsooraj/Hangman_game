from random import randint

def pick_random_word():
    with open("words.txt", 'r') as words_file:
        word_list=words_file.readlines() #list of Words from readlines() method
        
    selected_index=randint(0,len(word_list)-1) #word is selected from the list
    return word_list[selected_index]
