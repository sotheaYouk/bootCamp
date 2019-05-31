from operator import itemgetter

# convert strings to numbers 
def strings_to_numbers(argument):

    argument = argument.upper()

    if argument.isdigit():
        argument = int(argument)
        
        return argument
    
    else:
        switcher = {
            'T': 10, 
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }

        return switcher.get(argument, "nothing")


# split the list into a list of card strings 
# takes the original list as input
def split_card(card_list):
    new_list = list()

    for elem in card_list:
        elem = strings_to_numbers(elem[0])
        new_list.append(elem)
    
    new_list.sort()
    return new_list


# split the list into a list of suit stings 
# takes the original list as input
def split_suit(card_list):
    new_list = list()

    for elem in card_list:
        elem = strings_to_numbers(elem[0])
        new_list.append(elem)
    
    new_list.sort()
    return new_list


# dictionary 
def occurence(my_dict):
    dictionary = {}

    for index in my_dict:

        if index not in dictionary:
            dictionary[index] = 1

        else: 
            dictionary[index] = dictionary[index] + 1

    return dictionary


# check no pair 
# takes card list as input 
def no_pair(card_list):
 
    count = 0

    # count occurence of each element in the list
    dictionary = occurence(card_list)

    for dict_values in dictionary.values():
        if dict_values == 1:
            count += 1

    if count == 5:
        return "No pair"

    else:
        return one_two_pair(dictionary, card_list)


# one and two pair 
# takes dictionary as input 
def one_two_pair(dictionary, card_list):
    count = 0 

    for dict_values in dictionary.values():
        if dict_values == 2:
            count += 1

    if count == 1:
        return "One pair"

    elif count == 2: 
        return "Two pair"

    else:
        return three_four_of_a_kind(dictionary, card_list)

# three and four of a kind 
# takes dictionary as input 
def three_four_of_a_kind(dictionary, card_list):
    for dict_values in dictionary.values():

        if dict_values == 3:
            return "Three of a kind"

        # elif dict_values == 4:
        #     return "Four of a kind"

        else:
            return straight(dictionary, card_list)


# straight 
# takes card list as input
def straight(dictionary, card_list):

    for index in range(5):
        if card_list[index + 1] == card_list[index]:
            is_straight = True 
    
    if is_straight == True: 
        return "straight"

    else:
        return flush(dictionary, card_list)


# flush
# Takes suit list as input 
def flush(dictionary, card_list):
    if card_list.count(card_list[0]) == 5:
        return "Flush"

    else:
        return "Not flush"


# main function
def poker_hand(player_one, player_two):
    
    player_two = player_two.split()

    


poker_hand("AK KH QH JH TH", "AS KS TS 2H 3H")