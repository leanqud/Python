def integerDivision(n, k):
    if n < k:
        return 0
    else:
        return 1 + integerDivision(n-k, k)


def collectEvenInts(listOfInt):
    if listOfInt == []:
        return []
    elif listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    if someString == "":
        return 0
    someString = someString.upper()
    if someString[0] == 'A' or someString[0] == 'E' or someString[0] == 'I' or someString[0] == 'O'or someString[0] == 'U':
        return 1 + countVowels(someString[1:])
    else:
        return countVowels(someString[1:])

def reverseString(s):
    if s == "":
        return s
    else:
        return reverseString(s[1:]) + s[0]
    

def removeSubString(s, sub):
    if s == "":
        return s
    n = len(sub)
    if s[0:n] == sub:
        return removeSubString(s[n:], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)
