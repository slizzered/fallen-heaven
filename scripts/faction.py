__author__ = 'cos'





class Faction(object):
    '''
    Holds the information about a faction i.e. a player and all its units and resources.
    '''
    name = None
    resources = None
    technology = None

    # _RES_ENERGY, _RES_CREDITS, _RES_RESEARCH = xrange(3)

    def __init__(self, name= ""):
        self.resources = {"Energy": 0,
                     "Credits" : 0,
                     "Research" : 0}

        self.technology = {"Energy" : 1,
                      "Armor" : 1,
                      "Movement" : 1,
                      "Damage" : 1,
                      "RateOfFire" : 1,
                      "Rocketry" : 1}

        self.name = name

        self.pwnedPlanets = ["firstCapital"]

    def __setInfo__(self, factionInfo):
        [setattr(self, info, factionInfo[info]) for info in factionInfo.keys()]

    def __getInfo__(self):

        factionDict = {}
        for member in dir(self):
            if not member.startswith("__"):
                factionDict[member] = getattr(self, member)

        return factionDict
