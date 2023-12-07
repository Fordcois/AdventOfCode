from inputDay07 import *
from collections import Counter

data_set=input_data
list_of_inputs= (data_set.split(('\n')))

class Hand:
    def __init__(self,hand_as_string):
        self.split_string=hand_as_string.split(' ')
        self.cards_in_hand = self.convert_hand_to_list(self.split_string[0])
        self.bid = int(self.split_string[1])
        self.jokers=self.split_string[0].count('J')
        self.hand_without_jokers=[x for x in self.cards_in_hand if x not in '1']
        if self.jokers==0:
            self.hand_type=self.check_poker_hand(self.cards_in_hand)
        else:
            self.hand_type=self.deal_with_jokers()
        self.ranking=self.give_ranking()
    

    def convert_hand_to_list(self,string):
        conversionDict = {'T':'10','J':'1','Q':'12','K':'13','A':'14'}
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
    
    def check_poker_hand(self,card_list):
        counts=Counter(card_list)
        if 5 in counts.values():
            return 6
        if 4 in counts.values():
            return 5
        # Full House (3 of a Kind + 2 of a kind)
        elif 3 in counts.values() and 2 in counts.values():
            return 4
        # Three of a Kind
        elif 3 in counts.values():
            return 3
        # Two Pairs
        elif list(counts.values()).count(2) == 2:
            return 2
        # One Pair
        elif 2 in counts.values():
            return 1
        else:
            # High Card
            return 0
        
    def deal_with_jokers(self):
        without_joker_score=self.check_poker_hand(self.hand_without_jokers)
        # Four of a Kind
        if without_joker_score == 5: 
            if self.jokers == 1:
            #   Becomes a Five of a Kind!
                return 6
        # Three of a Kind
        if without_joker_score == 3: 
            # 2 Jokers
            if self.jokers == 2:
            #   becomes 5 of a kind
                return 6
            if self.jokers == 1:
            #   Becomes 4 of a Kind
                return 5
        # Two Pairs
        if without_joker_score == 2: 
            if self.jokers == 1:
            #   Becomes a Full House
                return 4
        # One Pair
        if without_joker_score == 1: 
                # 3 Jokers
                if self.jokers == 3:
                #   Becomes 5 of a Kind
                    return 6
                # 2 Jokers
                if self.jokers == 2:
                #   Becomes 4 of a kind
                    return 5
                # 1 Joker
                if self.jokers == 1:
                #   Becomes 3 of a Kind
                    return 3
        # High Card
        if without_joker_score == 0: 
                # 5 Jokers
                if self.jokers == 5:
                #   Becomes 5 of a Kind
                    return 6
                # 4 Jokers
                if self.jokers == 4:
                #   Becomes 5 of a kind
                    return 6
                # 3 Jokers
                if self.jokers == 3:
                #   Becomes 3 of a Kind
                    return 5
                # 2 Jokers
                if self.jokers == 2:
                #   Becomes 1 pair
                    return 3
                # 1 Jokers
                if self.jokers == 1:
                #   Becomes 1 pair
                    return 1
        return (without_joker_score)
        
    def __repr__(self) -> str:
        return f"Hand: {self.split_string[0]}  Bid: {self.bid} Ranking: {self.ranking}"


list_of_hand_objects = [Hand(x) for x in list_of_inputs]
sorted_list = sorted(list_of_hand_objects, key=lambda hand: hand.ranking)

GameScore=0
for index,hand in enumerate(sorted_list):
    GameScore+=(hand.bid*(index+1))

print (f'The Total Score is: {GameScore}')
# The Total Score is: 248652697
