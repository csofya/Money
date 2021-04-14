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
        
    ognum = 0   
    # first check if mon is a float or int
    # if mon has cents in it...
    if (isinstance(mon, int) == False):
        # last two digits will be cents
        # I used floor, because sometimes when dividing, there's still a decimal
        mon = math.floor(mon * 100)
        onescent = mon % 10
        if onescent in numberones:
        # we can use the same dictionary for ones place
            onescentstr = numberones[onescent] 
            tenscent = ((mon - onescent) / 10) % 10
            if (tenscent == 0):
                totalcents = ' and ' + onescentstr + ' cents'
            elif (tenscent == 1):
                teenscent = teen[onescent]
                totalcents = ' and ' + teenscent + ' cents'
            else:
                tenscentstr = numbertens[tenscent]
                totalcents = ' and ' + tenscentstr + ' ' + onescentstr + ' cents'
        elif onescent == 0:
            tenscent = 1
            totalcents =  ' and ten cents'
        # in order to get the non-decimal number, we can keep track
        # by subtracting the added cents and dividing by 100
        ognum = (tenscent * 10) + onescent
        mon = (mon - ognum)/100
    else:
        totalcents = ''

    # iterate through each number
    ones = mon % 10 
   
    # get the value from ones dictionary
    if ones in numberones:
        onestring = numberones[ones] 
    else:
        onestring = ''
    # get the tens digit through arithmetic
    tens = (mon - ones) / 10

    if tens in numbertens:
        tensstring = numbertens[tens] # last is 3, value is three
        result = tensstring + ' ' + onestring + ' dollars' + totalcents
        
    # else if the tens digit is one, go the teens dicionary
    elif tens == 1:
        teenstring = teen[ones]
        result = teenstring + ' dollars' + totalcents
    
    # if there is only one digit, just print the ones string
    else: 
        result = onestring + ' dollars' + totalcents
        
    return result

print(from_mon_to_eng(91.92)) 
print(from_mon_to_eng(82)) 
print(from_mon_to_eng(13.02)) 
print(from_mon_to_eng(80.76)) 
print(from_mon_to_eng(36.16)) 
print(from_mon_to_eng(10.99)) 

# for i in range(0, 100):
#     print(from_mon_to_eng(i))
