from inputDay06 import *
import re

numbers_list = re.findall(r'\d+', input_data) 

half_length = len(numbers_list) // 2
race_data = [[int(numbers_list[i]), int(numbers_list[i + half_length])] for i in range(half_length)]

def how_many_ways_to_win(race_array):
    ways_to_beat_race=0
    time=race_array[0]
    record_distance=race_array[1]
    for seconds_held in range(1,time):
        distance_travelled = seconds_held*(time-seconds_held)
        if distance_travelled > record_distance:
            ways_to_beat_race+=1
    return ways_to_beat_race


def part_one():
    ways_to_win_each_race=[ how_many_ways_to_win(x) for x in race_data]
    result = 1
    for ways_to_win in ways_to_win_each_race:
        result *= ways_to_win
    print (f'There are {result} Ways to beat these elves!')

part_one()
# 138915

