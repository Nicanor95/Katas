# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python

'''
The professor will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits. The only 
operators he knows are addition (+),subtraction(-), and 
multiplication (*), so those are the only ones that will appear. 
Each number will be in the range from -1000000 to 1000000, and will 
consist of only the digits 0-9, possibly a leading -, and maybe a 
few ?s. If there are ?s in an expression, they represent a digit 
rune that the professor doesn't know (never an operator, and never 
a leading -). All of the ?s in an expression will represent the same 
digit (0-9), and it won't be one of the other given digits in the 
expression. No number will begin with a 0 unless the number itself 
is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented 
by the question mark. If more than one digit works, give the lowest 
one. If no digit works, well, that's bad news for the professor - 
it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of 
the unknown rune. The method takes a string as a paramater repressenting 
the expression and will return an int value representing the unknown 
rune or -1 if no such rune exists.
'''
import re

def solve_runes(runes):
    # Get already solved digits.
    known = list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), runes)))
    unknown = list(filter(lambda x: x not in known, range(10)))

    # Find type of operation.
    operator = list(filter(lambda x: x in ['+', '-', '*'], runes[1:]))[0]

    # Split the operation.
    numbers = re.split(r'(?<=\d|\?)(\{}|=)'.format(operator), runes)
    numbers = list(filter(lambda x: x != operator and x != '=', numbers))

    for x in unknown:
        replaced = list(map(lambda n: n.replace('?', str(x)), numbers))
        if (any([True if re.search(r'(?<!\d)0(?=\d)', number) else False for number in replaced])):
            continue
        elif (eval(replaced[0] + operator + replaced[1] + '==' + replaced[2])):
            return x

    return -1