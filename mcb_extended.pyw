#! python3
# mcb_extended.pyw - Saves, loads, and deletes pieces of text to the clipboard.
# Usage: py.exe/python3 mcb_extended.pyw save <keyword> - Saves clipboard to keyword
#        py.exe/python3 mcb_extended.pyw <keyword> - Loads keyword to clipboard.
#        py.exe/python3 mcb_extended.pyw list - Loads all keywords to clipboard.
#        py.exe/python3 mcb_extended.pyw delete<keyword> - deletes keyword from the shelf
#        py.exe/python3 mcb_extended.pyw delete_all = deletes all keywords

import shelve, pyperclip, sys, pyinputplus

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# creating shelf file and adding data
mcbExtendedShelf = shelve.open('mcb_extended')
#print(list(mcbExtendedShelf))

mcbExtendedShelf['agree'] = TEXT['agree']
mcbExtendedShelf['busy'] = TEXT['busy']
mcbExtendedShelf['upsell'] = TEXT['upsell']
# print(list(mcbExtendedShelf.keys()))
# print(list(mcbExtendedShelf.values()))

if len(sys.argv) < 2:
    print('''Usage:  py.exe/python3 mcb_extended.pyw save <keyword> - Saves clipboard to keyword.
        py.exe/python3 mcb_extended.pyw <keyword> - Loads keyword to clipboard.
        py.exe/python3 mcb_extended.pyw list - Loads all keywords to clipboard.
        py.exe/python3 mcb_extended.pyw delete<keyword> - deletes keyword from the shelf
        py.exe/python3 mcb_extended.pyw delete_all = deletes all keywords''')
    sys.exit()
else:
    print('sys.argv[1]:', str(sys.argv[1]))
# Save clipboard content to the provided keyword
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            mcbExtendedShelf[sys.argv[2]] = pyperclip.paste()
            print(f'Text for {sys.argv[2].lower()} at the clipboard copied to the list.')
        elif sys.argv[1].lower() == 'delete':
            del mcbExtendedShelf[sys.argv[2]]
            print(f'Text for {sys.argv[2].lower()} deleted from the list.')
# List keywords
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbExtendedShelf.keys())))
            print('List of keywords copied to clipboard.')
            print(list(mcbExtendedShelf))
# Loads content
        elif sys.argv[1].lower() in mcbExtendedShelf:
            pyperclip.copy(mcbExtendedShelf[sys.argv[1].lower()])
            print(f'Text for {sys.argv[1].lower()} copied to clipboard.')
            print(str(mcbExtendedShelf[sys.argv[1].lower()]))
# Deletes all keywords
        elif sys.argv[1].lower() == 'delete_all':
            confirmation = pyinputplus.inputYesNo(prompt="Do you want to delete all keywords in the list (type 'YES' to confirm)? ", \
                                                  caseSensitive=True, yesVal="YES")
            if confirmation == 'YES':
                mcbExtendedShelf.clear()
                print('List of keywords deleted.')
                print('list: ', list(mcbExtendedShelf))

mcbExtendedShelf.close()