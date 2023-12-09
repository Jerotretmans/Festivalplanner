with open('timetable_friday_2023.csv', 'r') as infile:
    lines = infile.readlines()

with open('new_defqon_2023_timetable.csv', 'w') as outfile:
    for line in lines:
        # Strip newline character from the original line and add ',1'
        modified_line = line.strip() + ',1\n'
        outfile.write(modified_line)