from inputDay06 import *
import re

numbers_list = re.findall(r'\d+', input_data) 

half_length = len(numbers_list) // 2

part_two_time=int("".join(numbers_list[0:half_length]))
part_two_distance=int("".join(numbers_list[half_length:]))

part_two_race_data=(part_two_time,part_two_distance)

def part_two():
    ways_to_beat_race=0
    time=part_two_time
    record_distance=part_two_distance
    for seconds_held in range(1,time):
        distance_travelled = seconds_held*(time-seconds_held)
        if distance_travelled > record_distance:
            ways_to_beat_race+=1
    print(f'You can beat these elves {ways_to_beat_race} ways')


part_two()
# You can beat these elves 27340847 ways

