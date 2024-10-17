from lab03 import *

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(1, 8) == 0
    assert integerDivision(25,5) == 5
    assert integerDivision(1,1) == 1

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([1,3,5]) == []
    assert collectEvenInts([2]) == [2]
    assert collectEvenInts([1,100,37,5,28]) == [100,28]

def test_countVowels():
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("stl") == 0
    assert countVowels("shellfish") == 2

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("") == ""
    assert reverseString("D") == "D"
    assert reverseString("Shelf") == "flehS"

def test_reverseSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("", "fish") == ""
    assert removeSubString("trunktrunktrunk", "run") == "tktktk"
