from inputDay07 import *
from collections import Counter

data_set=input_data
list_of_inputs= (data_set.split(('\n')))

class Hand:
    def __init__(self,hand_as_string):
        self.split_string=hand_as_string.split(' ')
        self.cards_in_hand = self.convert_hand_to_list(self.split_string[0])
        self.bid = int(self.split_string[1])
        self.hand_type=self.check_hand()
        self.ranking=self.give_ranking()

    def convert_hand_to_list(self,string):
        conversionDict = {'T':'10','J':'11','Q':'12','K':'13','A':'14'}
        converted_hand = [x if x.isnumeric() else conversionDict[x] for x in string]
        return converted_hand
    
    def give_ranking(self):
        ranking=''
        for card in self.cards_in_hand:
            if len(card)==1:
                ranking += f'0{card}'
            else:
                ranking += card
        return float(f"{self.hand_type}.{ranking}")
    
    def check_hand(self):
        counts=Counter(self.cards_in_hand)
        if 5 in counts.values():
            # return "Five of a Kind"
            return 6
        if 4 in counts.values():
            # return "Four of a Kind"
            return 5
        elif 3 in counts.values() and 2 in counts.values():
            return 4
        elif 3 in counts.values():
            # return "Three of a Kind"
            return 3
        elif list(counts.values()).count(2) == 2:
            # return "Two Pairs"
            return 2
        elif 2 in counts.values():
            # return "One Pair"
            return 1
        else:
            # return "High Card"
            return 0
        
    def __repr__(self) -> str:
        return f"Hand: {self.split_string[0]} Bid:{self.bid} Rank:{self.ranking}"


list_of_hand_objects = [Hand(x) for x in list_of_inputs]
sorted_list = sorted(list_of_hand_objects, key=lambda hand: hand.ranking)

GameScore=0
for index,hand in enumerate(sorted_list):
    GameScore+=(hand.bid*(index+1))

print (f'The Total Score is: {GameScore}')
# The Total Score is: 250453939
