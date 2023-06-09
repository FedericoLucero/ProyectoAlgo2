class Distance:
    Distance = None #int
    NearNodeInWay = None #str
    

class Corner:
   Name = None #str
   DistantTo = None #int
   
class Address:
   CornerOrigin = Corner  #(CornerOrigin)
   CornerDestiny = Corner  #(CornerDestiny)

class FixUbication:
    Address = Address #tipo clase Address
    
class MobileUbication:
    Address = None #tipo clase Address
    Amount = None #int
    
    