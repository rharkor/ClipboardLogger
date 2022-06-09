import pyperclip
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# Read FILE_LOCATION from env
file_location = os.getenv("FILE_LOCATION")
file = open(file_location, "a+")
file.close()

def get_current_date():
    # Get the date with the format "YYYY-MM-DD HH:MM:SS"
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def handle_change(recent_value):
    while True:
        _ = pyperclip.paste()
        if _ != recent_value:
            # Write to file
            current_date = get_current_date()
            file = open(file_location, "a+")
            file.write(current_date + ": " + _ + "\n")
            file.close()
            
            recent_value = _
            print('Written to file:', recent_value)

def main():
    recent_value = ""
    handle_change(recent_value)

if __name__ == '__main__':
    main()