from inputDay04 import *
list_of_cards= inputdata.split('\n')

total_score=0

def check_card(card):
    global total_score
    score=0
    just_numbers=(card.split(':')[1]).split('|')
    scratched_off_numbers=[int(x) for x in just_numbers[0].split(' ') if x!= '']
    winning_numbers=[int(x) for x in just_numbers[1].split(' ') if x!= '']
    matched_numbers=[x for x in scratched_off_numbers if x in winning_numbers]
    if matched_numbers != []:
        score = 2 ** ((len(matched_numbers))-1)
    total_score+=score

for card in list_of_cards:
    check_card(card)

print(f'Total Score is: {total_score}')
# Total Score is: 24175