# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Import statements
import json
import os
import TwitterAPI

api = TwitterAPI.TwitterAPI('COjeauC1T6JGito94EV8xbbkL', 'IBTZMVYXmMcUZ5RIi9tjLI7Gd4ybYiLA4mp44XZAdBwQkOMbz6')

# Saving credentials to a json file
filename = "twitter_credentials.json"
if not os.path.exists(filename):
    api.create_credential_file



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
