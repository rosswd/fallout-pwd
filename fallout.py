# Fallout password terminal challenge

# intro message
print('''
    Welcome to the Fallout Terminal Management System.
    Details about the services offered by this Terminal are listed below.
    Have a nuclear day! 

                    Mushroom Corp. Security Systems.

    =====================================================================

    Good day comrade! This terminal offers access to three separate
    systems, each requiring a greater level of clearance than the last.

    Those areas are: 
        (1) Billing
        (2) Human Resources
        (3) Mainframe Access

    This Terminal is generation two, meaning, when you make a mistake
    entering a password, you are told how many characters you got wrong.
    Based on your required level of access your are allowed so many tries 
    before Central are notifed and your activity relayed.

    | No. | System           | Tries | Passwords | Password Length |
    |-----|------------------|-------|-----------|-----------------|
    | (1) | Billing          |   5   |     8     |         6       |
    | (2) | Human Resources  |   4   |    10     |        10       |
    | (3) | Mainframe Access |   3   |    12     |        15       |

    Enter a choice of 1, 2 or 3 to begin:
''')

# create password lists
billingPasswords = ['kreolo', 'treelo', 'grillo', 'kraalo', 'ubollo', 'araalo', 
'buzalo', 'pifzlo']

hrPasswords = ['reticulate', 'arbicolase', 'seticolair', 'ratelicare', 
'vrabilbase', 'resacubate', 'rehashfate', 'fatarketea', 'ubekgadare', 
'subloglare']

mfPasswords = ['worshipfully', 'whimsicality', 'wherethrough', 
'watermanship', 'watchfulness', 'weatherboard', 'wattenscheid', 'weatherglass',
'westernizing', 'wretchedness', 'whoremastery', 'westernising', 'wollastonite',
'wordlessness', 'wirelessness']

# set correct passwords
billingSecret = billingPasswords[3]
hrSecret = hrPasswords[0]
mfSecret = mfPasswords[9]

# set number of allowed tries
billingGuesses = 5
hrGuesses = 4
mfGuesses = 3

# checks how many characters are correct
def check_guess(userGuess, levelSecret):
    correct = 0
    for g, s in zip(userGuess, levelSecret):
        if g == s:
            correct += 1
    return correct

# ask for input and check guess against actual password
def start_auth(guesses, levelSecret):
    guessCount = 0
    while guessCount < guesses:
        print('\nPassword ' + '(Attempt ' + str(guessCount+1) + '/' + str(guesses) + ')' + ':')
        userGuess = raw_input('> ')

        if len(userGuess) < len(levelSecret) or len(userGuess) > len(levelSecret):
            print('You must enter ' + str(len(levelSecret)) + ' characters.')
            break
    
        if userGuess == levelSecret:
            print('System Unlocked. Do thy worst.')
            break
    
        result = check_guess(userGuess, levelSecret)
        print(str(result) + ' correct ' + str(len(levelSecret) - result) + ' incorrect')
        guessCount += 1
    
        if guessCount == guesses:
            print('\nFAILURE TO AUTHENTICATE\n \nCentral have been alerted... \nYou have 60 secs before a drone arrives.')

# get difficulty level
systemLevel = raw_input('> ')

# print passwords based on entered difficulty
print('\nHere\'s your password list, choose wisely:\n')

def print_passwords(passwdList):
    for p in passwdList:
        print(p)

# main program which print the list of passwords and runs the guess checker
def set_difficulty():
    if systemLevel == '1':
        print_passwords(billingPasswords)
        start_auth(billingGuesses, billingSecret)
    elif systemLevel == '2':
        print_passwords(hrPasswords)
        start_auth(hrGuesses, hrSecret)
    elif systemLevel == '3':
        print_passwords(mfPasswords)
        start_auth(mfGuesses, mfSecret)
    else:
        print('Not a valid choice, enter 1, 2 or 3')

set_difficulty()
