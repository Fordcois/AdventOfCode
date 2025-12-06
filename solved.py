import os
from pathlib import Path

def solved():
    start_table_index = None
    end_table_index = None

    user_input_year = input('What year is it (YYYY)?    ').strip()
    if not(user_input_year.isdigit() and len(user_input_year) == 4):
        print('ERROR - Invalid Year')
        return False
                
    user_input_day = input('What Day is it?    ').strip()
    if not user_input_day.isdigit():
        print('ERROR - Invalid Day')
        return False

    user_input_stars = int(input('Which part is complete?    ').strip())
    if user_input_stars not in (1,2):
        print('ERROR - Invalid Stars')
        return False
    
    with open('README.md', 'r', encoding='utf-8') as f:
        file_content = f.readlines()

    for index,line in enumerate(file_content):
        if f'<summary>{user_input_year}' in line:
            start_table_index = index

        if f'(https://adventofcode.com/{user_input_year}/day/{user_input_day})' in line:
            day_line_index = index

        if f'</details EndOf{user_input_year}Table>' in line:
            end_table_index = index

    if start_table_index is None or end_table_index is None or day_line_index is None:
        print ('ERROR! - No Day Found')
        pass

    split_line =  [x.strip() for x in file_content[day_line_index].split('|')]
    file_content[day_line_index] = f"| {split_line[1]} | {split_line[2]} | {'⭐️' * user_input_stars} |\n"

    
    stars = sum(line.count('⭐️') for line in file_content[start_table_index+2 : end_table_index])
    file_content[start_table_index] = f'<summary>{user_input_year} - ⭐️ {stars} Stars</summary>\n'

    print (f'Congratulations on Solving Day {user_input_day} - You have {stars} stars for {user_input_year}')

    # Write the updated content back to the file
    with open('README.md', 'w', encoding='utf-8') as f:
        f.writelines(file_content)

    



if __name__ == "__main__":
    solved()