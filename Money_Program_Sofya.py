'''
$0 - $99
input: 32
output: Thirty two dollars
'''

import math

numberones = {
    # 0: 'zero', 
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

numbertens = {
    #0: 'zero', 
    #1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

teen = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

# to convert money amount into english
def from_mon_to_eng(mon):
    
    # validates if money is between $0 - $99
    if (mon < 0 or mon > 99):
        return False
    if (mon == 0):
        return 'zero dollars'
        
    # first check if mon is a float or int
    # if mon has cents in it...
    if (isinstance(mon, int) == False):
        cents = math.ceil((mon % 1) * 100)
        # if (cents > )
        if (cents > 9):
            onescent = (cents % 10)
            if (onescent == 0):
                tenscent = math.ceil((cents - onescent) / 10)
                tenscentstr = numbertens[tenscent]
                totalcents = 'and ' + tenscentstr + ' cents'
            else:
                onescentstr = numberones[onescent]
                tenscent = math.floor((cents - onescent) / 10)
                tenscentstr = numbertens[tenscent]
                totalcents = 'and ' + tenscentstr + ' ' + onescentstr + ' cents'
        else:
            onescent = math.floor(cents % 10)
            onescentstr = numberones[onescent]
            totalcents = 'and ' + onescentstr + ' cents'
    else:
        totalcents = ''
    mon = mon - (mon % 1)
    # iterate through each number
    ones = mon % 10 
    
    if (ones == 0):
        onestring = ''
    else:
        # get the value from ones dictionary
        onestring = numberones[ones] 
    
    # get the tens digit through arithmetic
    tens = (mon - ones) / 10

    if tens in numbertens:
        tensstring = numbertens[tens] # last is 3, value is three
        result = tensstring + ' ' + onestring + ' dollars ' + totalcents
        
    # else if the tens digit is one, go the teens dicionary
    elif tens == 1:
        teenstring = teen[ones]
        result = teenstring + ' dollars ' + totalcents 
    
    # if there is only one digit, just print the ones string
    else: 
        result = onestring + ' dollars ' + totalcents 
        
    return result
    
print(from_mon_to_eng(91.92)) 
print(from_mon_to_eng(82)) 
print(from_mon_to_eng(13.02)) 
print(from_mon_to_eng(80.76)) 

# for i in range(0, 100):
#     print(from_mon_to_eng(i))
