class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
               .strip().format(self.rent, self.metersFromUCSB, self.condition)

    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == "excellent":
                    return True
                elif self.condition == "average" and other.condition != "excellent":
                    return True
        return False

    def __eq__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    if self.condition == "excellent" and other.condition == "excellent":
                        return True
                    elif self.condition == "average" and other.condition == "average":
                        return True
                    elif self.condition == "bad" and other.condition == "bad":
                        return True
        return False
