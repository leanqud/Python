from Apartment import Apartment

def mergesort(aparmentList): #2
    if len(aparmentList) > 1:
        mid = len(aparmentList) // 2
        lefthalf = aparmentList[:mid]
        righthalf = aparmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                aparmentList[k] = lefthalf[i]
                i = i + 1
            else:
                aparmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            aparmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            aparmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList): #1
    if len(apartmentList) == 1:
        return True
    else:
        if apartmentList[0] < apartmentList[1]:
            return ensureSortedAscending(apartmentList[1:])
    return False

def getBestApartment(apartmentList): #3
    if apartmentList == 1:
        return apartmentList.getApartmentDetails()
    else:
        mergesort(apartmentList)
        best = apartmentList[0]
        return best.getApartmentDetails()

def getWorstApartment(apartmentList): #3
    if apartmentList == 1:
        return apartmentList.getApartmentDetails()
    else:
        mergesort(apartmentList)
        worst = apartmentList[-1]
        return worst.getApartmentDetails()

def getAffordableApartments(apartmentList, budget): #4
    mergesort(apartmentList)
    affordableList = []
    count = 0
    for i in apartmentList:
        if apartmentList[count].getRent() <= budget:
            affordableList.append(apartmentList[count].getApartmentDetails())
            count += 1
    affordableList = '\n'.join(affordableList)
    return affordableList
        









        
