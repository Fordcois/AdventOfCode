import os
from pathlib import Path

# Adjust Year
year=2024

def create_new_day():
    while True:
        user_input_day = input('What Day is it? ').strip()
        # Validate & clean input
        if not user_input_day.isdigit():
                print('ERROR - Invalid Number')
                break
        day_number = f'{int(user_input_day):02d}'
            
        # Create folder path
        folder_path = f'{year}/Day{day_number}'
            
        if os.path.exists(folder_path):
            print(f'Folder called Day{day_number} in {year} already exists')
            break
        
        else:
            folder_path=f'{year}/Day{day_number}'
            print (f'Creating Day{day_number} in {year}')
            os.makedirs(folder_path)

            # Create Empty __init__.py
            Path(f'{folder_path}/__init__.py').touch()
            # Create Empty real_input.txt
            Path(f'{folder_path}/real_input.txt').touch()
            # Create Empty test_input.txt
            Path(f'{folder_path}/test_input.txt').touch()

            # Template text for the Puzzle files
            template_text = """# Adjust Import Paths
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.ParseTXTAsList import Parse_Txt_as_List

# Substitue test/real to switch inputs
data_set = 'real'
data = Parse_Txt_as_List(f'{data_set}_input.txt')
from utils.ParseTXTAsList import Parse_Txt_as_List

# Puzzle
def solve():
    return

solve()"""
            # Create Part One
            with open(f'{folder_path}/aoc{year}{day_number}Part01.py', 'w') as file:
                file.write(template_text)

            # Create Part Two
            with open(f'{folder_path}/aoc{year}{day_number}Part02.py', 'w') as file:
                file.write(template_text)
            
            # Template text for the Test file
            test_template_text = f"""from .aoc{year}{day_number}Part01 import *
from .aoc{year}{day_number}Part02 import *
# Test Suites are included to aid during development and debugging and may not offer a complete overview and solution

def test_connection():
    assert 'Hello World' == 'Hello World'"""
            
            # Create Test File
            with open(f'{folder_path}/test_aoc{year}{day_number}.py', 'w') as file:
                file.write(test_template_text)

            # Update the MD File:
            puzzle_name = input("What is today's puzzle name? ").title().strip()

            # Read the current content of the file to find the last line of the table
            with open('README.md', 'r') as f:
                file_content = f.readlines()
            
            last_line_of_table = len(file_content)
            
            for line_index,line_content in enumerate(file_content):
                if line_content.strip() == f'</details EndOf{year}Table>':
                    last_line_of_table = line_index
                    break
            
            # Append the new row
            file_content.insert(last_line_of_table, f'| [Day {int(day_number)}: {puzzle_name}](https://adventofcode.com/{year}/day/{int(day_number)}) | [Solution](https://github.com/Fordcois/AdventOfCode/tree/main/{year}/Day{day_number}) | | \n')
            
            # Write the updated content back to the file
            with open('README.md', 'w') as f:
                f.writelines(file_content)

            print (f'Day {day_number} - {puzzle_name} established - Good Luck!')
            return

if __name__ == "__main__":
    create_new_day()