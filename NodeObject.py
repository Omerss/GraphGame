
class NodeObject():

    colour = ""
    shape = ""
    location = {'x':0, 'y':0}
    size = 0
    neighbors = []

    def __init__(self, location, size, color = "black", shape = "square"):
        pass




class Neighbor():
    nodeid = -1
    angle = -1
    dist = -1


    def __init__(self,newID,newAngle,newDist):
        nodeid = newID
        angle = newAngle
        dist = newDist




