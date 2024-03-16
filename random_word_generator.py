from random import randint

def pick_random_word():
    #list of words
    word_list=["Hulk"]

    selected_index=randint(0,len(word_list)-1) #word is selected from the list
    return word_list[selected_index]
