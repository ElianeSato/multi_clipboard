#! python3
# mcb_extended.pyw - Saves, loads, and deletes pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete<keyword> - deletes keyword from the shelf
#        py.exe mcb.pyw delete_all = deletes all keywords

import shelve, pyperclip, sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# creating shelf file and adding data
mcbExtendedShelf = shelve.open('mcb_extended')
print(list(mcbExtendedShelf))
# mcbExtendedShelf = shelve.open('mcb_extended')['agree'] = TEXT['agree']
# mcbExtendedShelf = shelve.open('mcb_extended')['busy'] = TEXT['busy']
# mcbExtendedShelf = shelve.open('mcb_extended')['upsell'] = TEXT['upsell']
# print(list(mcbExtendedShelf.keys()))
# print(list(mcbExtendedShelf.values()))


# adding list of command lines to sys.argv, where sys.argv = script's name
# sys.argv.append('save')
# sys.argv.append('spam')
# sys.argv.append('I hate spams')
# print(list(sys.argv))
# print(len(sys.argv))

# original command
if len(sys.argv) < 2:
    print('Usage: python mcbExtendedShelf.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line is the keyphrase
print(f'keyphrase: {keyphrase}')

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyword])
    print('Text for ' + keyphrase + 'copied to clipboard.')
else:
    print("There is no text for " + keyphrase)

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbExtendedShelf[sys.argv[2]] = pyperclip.paste()
    print(list(mcbExtendedShelf))
# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbExtendedShelf.keys())))
    elif sys.argv[1] in mcbExtendedShelf:
        pyperclip.copy(mcbExtendedShelf[sys.argv[1]])

#keyphrase = 'sorry'
if keyphrase in mcbShelf:
    pyperclip.copy(mcbShelf[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

mcbShelf.close()