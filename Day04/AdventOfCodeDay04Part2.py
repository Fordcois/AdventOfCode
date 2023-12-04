from inputDay04 import *
list_of_cards= inputdata.split('\n')

cards_dict={}

def check_card(card):
    just_numbers=(card.split(':')[1]).split('|')
    scratched_off_numbers=[int(x) for x in just_numbers[0].split(' ') if x!= '']
    winning_numbers=[int(x) for x in just_numbers[1].split(' ') if x!= '']
    matched_numbers=[x for x in scratched_off_numbers if x in winning_numbers]
    return len(matched_numbers)

def add_to_collection (card):
    global cards_dict
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

for index,card in enumerate(list_of_cards):
    add_to_collection(card)
    copies_of_card=cards_dict[card]
    wins=check_card(card)
    for i in range (wins):
        for y in range(copies_of_card):
            add_to_collection(list_of_cards[(index+1)+i])

print (f'You Scratched off: {sum(list(cards_dict.values()))}')
