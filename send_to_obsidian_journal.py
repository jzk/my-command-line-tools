import sys
import os
import shutil
from datetime import date

from datetime import datetime

"""
This Python script appends the first argument of the main function 
as a text entry to the current day's journal in Obsidian. 

The script is configured to work in conjunction with a workflow 
in Alfred, meaning it is initiated through an Alfred command 
that passes the argument. 

In context of Alfred workflow, the first argument is provided by 
what is typed into Alfred input before triggering the workflow.
"""


def get_current_time_string():
    current_time = datetime.now()

    # Format time as string
    return current_time.strftime("%H:%M")


def get_today_journal_filename():
    today = date.today()
    return "/Users/jzk/Dropbox/Apps/Obsidian/Notes/journals/" + today.strftime("%Y-%m-%d.md")


def validate_today_journal(filename):
    if os.path.exists(filename):
        print('File exists')
    else:
        print('File does not exist, creating one from template')
        shutil.copy('/Users/jzk/Dropbox/Apps/Obsidian/templates/Daily Planner.md', filename) 

def insert_text(filepath, new_text):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    insert_index = 0
    for index, line in enumerate(lines):
        if line.strip() == "# Journal":
            insert_index = index + 1
            last_empty_line_index = None

            while(not lines[insert_index].startswith("#") and insert_index < len(lines)-1):
                ## scan 如果是空，就记录一下last 空
                if(lines[insert_index].strip() == ""):
                    last_empty_line_index = insert_index
                else:
                    last_empty_line_index = None
                insert_index += 1
            break

    lines.insert(last_empty_line_index if last_empty_line_index is not None else insert_index, new_text +"\n")

    with open(filepath, 'w') as file:
        file.writelines(lines)



def main():
    note = sys.argv[1]
    print(note)

    today_journal_filename = get_today_journal_filename()

    validate_today_journal(today_journal_filename)

    insert_text(today_journal_filename, "- %s %s" % (get_current_time_string(), note))


main()    

