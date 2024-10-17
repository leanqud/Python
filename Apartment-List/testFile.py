from Apartment import Apartment
from lab06 import *

def test_Apartment():
    a0 = Apartment(1204, 200, "bad")
    print(a0.getApartmentDetails())

def test_overloadingOperators():
    a0 = Apartment(4, 4, "excellent")
    a1 = Apartment(5, 5, "bad")
    assert a1 > a0 == True
    a2 = Apartment(950, 215, "bad")
    a3 = Apartment(950, 215, "average")
    assert a2 > a3 == True
    a4 = Apartment(950, 215, "bad")
    a5 = Apartment(950, 215, "bad")
    assert a4 == a5 == True

def test_lab06_1():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    print('apartmentList is NOT SORTED:')
    for apartment in apartmentList: 
        print(apartment.getApartmentDetails())

    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

    print('apartmentList is SORTED:')
    for apartment in apartmentList: 
        print(apartment.getApartmentDetails())

def test_lab06_2():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert ensureSortedAscending(apartmentList) == False

    print('Best Apartment in apartmentList:')
    print(getBestApartment(apartmentList))

    print('Worst Apartment in apartmentList:')
    print(getWorstApartment(apartmentList))

def test_lab06_3():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    print('All apartments whose rent is <= in SORTED order:')
    print(getAffordableApartments(apartmentList, 950))

def test_edgeCases():
    a0 = Apartment(1115, 215, "bad")
    apartmentList = [a0]
    assert getAffordableApartments(apartmentList, 950) == ""

















    
