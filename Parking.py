
lots = []

def findSpot(occupantID):
 
    return

def parkedSpot(occupantID):
    return

def toSpot(occupantID):
    return

def leftSpot(occupantID):
    return

def changeLot(occupantID):
    return

def getLot(occupantID):
    return

def getOccupantLocation(occupantID, occupantLocation):
    return

def setOccupantLocation(occupantID, occupantLocation):
    return

class ParkingLot:
    # Stores parking spots and manages where user's are

    def __init__(self):
        # spots stores parking spots and their respective locations 
        self.__lot = {}
        self.__spotsRemaining = 0
        self.__range = ()
        return
    
    # goes through and find the spot with matches the user coordinates, then stores parking info
    def matchToSpot(self, occupantID, occupantLocation):
        for spot in self.__lot:
            # checks if user is in the spot
            if (self.__inLocation(occupantLocation, self.__lot[spot])):
                spot.setOccupation(True)
                spot.setOccupant(occupantID)
                self.__spotsRemaining += 1
                return spot
    
    # removes user from parking spot, leaving it empty
    def leavingSpot(self, spot):
        spot.setOccupation(False)
        spot.setOccupant = 0
        self.__spotsRemaining -= 1
    
    def getLot(self):
        return self.__lot
    
    def setSpotLocation():
        return
    
    # check if a location is in the lots' range specifically
    def inLot(self, loctation):
        self.__inLocation()
        return False
    
    # check if a location is in a range
    def __inLocation(self, location, lacationRange):
        return False
        


class ParkingSpot:
    # stores parking spot data: if its occupied or not and who's occupying it
    def __init__(self):
        self.__isOccupied = False
        self.__occupantID = 0
        return

    def setOccupation(self, occupation):
        self.__isOccupied = occupation
        return
        
    def getOccupation(self):
        return self.__isOccupied

    def setOccupant(self, occupant):
        self.__occupantID = occupant
        return
        
    def getOccupant(self):
        return self.__occupantID

# class User:
#     def __init__(self):
#         self.__isOccupied = False
#         self.__occupantID = 0
#         return