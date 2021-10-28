#! python3
# mcb_extended.pyw - Saves, loads, and deletes pieces of text to the clipboard.
# Usage: py.exe/python3 mcb_extended.pyw save <keyword> - Saves clipboard to keyword
#        py.exe/python3 mcb_extended.pyw <keyword> - Loads keyword to clipboard.
#        py.exe/python3 mcb_extended.pyw list - Loads all keywords to clipboard.
#        py.exe/python3 mcb_extended.pyw delete<keyword> - deletes keyword from the shelf
#        py.exe/python3 mcb_extended.pyw delete_all = deletes all keywords

import shelve, pyperclip, sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# creating shelf file and adding data
mcbExtendedShelf = shelve.open('mcb_extended')
print(list(mcbExtendedShelf))

mcbExtendedShelf['agree'] = TEXT['agree']
mcbExtendedShelf['busy'] = TEXT['busy']
mcbExtendedShelf['upsell'] = TEXT['upsell']
print(list(mcbExtendedShelf.keys()))
print(list(mcbExtendedShelf.values()))


# original command
if len(sys.argv) < 2:
    print('Usage: python3 mcbExtendedShelf.pyw [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line is the keyphrase
print(f'keyphrase: {keyphrase}')

if keyphrase in mcbExtendedShelf:
    pyperclip.copy(mcbExtendedShelf[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print("There is no text for " + keyphrase)

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbExtendedShelf[sys.argv[2]] = pyperclip.paste()
# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbExtendedShelf.keys())))
    elif sys.argv[1] in mcbExtendedShelf:
        pyperclip.copy(mcbExtendedShelf[sys.argv[1]])

#keyphrase = 'sorry'
if keyphrase in mcbExtendedShelf:
    pyperclip.copy(mcbExtendedShelf[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

mcbExtendedShelf.close()