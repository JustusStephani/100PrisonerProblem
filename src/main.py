import numpy as np
import numpy.typing as npt

from random import randint, shuffle

class PrisionExperiment:

    def __init__(self, numberOfPrisoners: int = 100, numberOFAttempts: int = 50) -> None:
        self.numberOfPrisoners = numberOfPrisoners
        self.drawerAttenumberOFAttemptsmpts = numberOFAttempts


    @staticmethod
    def getRandomList(lenOfList) -> npt.NDArray:
        randomList = np.arange(0, lenOfList, dtype=int)
        shuffle(randomList)
        return randomList


    def singlePrisonerAttemptingDraws(self, prisioner: int, shelfOfDrawers: npt.NDArray) -> int:
        drawerNumber = prisioner
        for attempt in range(0, self.numberOFAttempts):
            drawnNumber = shelfOfDrawers[drawerNumber]
            if drawnNumber == prisioner:
                return 1
            else:
                drawerNumber = drawnNumber
        return 0


    def performExperiment(self,) -> int:
        # Build a shelf with "numberOfPrisoners" draws 
        # The index of the array are the visible external numbers.
        # The int of the array are the hidden internal numbers, which are
        # randomly arranged.
        shelfOfDrawers = self.getRandomList(self.numberOfPrisoners)

        # The prisoners are a randomly arranged list of numbers.
        # The index is not important.
        prisoners = self.getRandomList(self.numberOfPrisoners)

        # Each prisioner is drawing one after each other, "numberOFAttempts" times unit
        # he finds his number. If he does not find his number the experiment is unsuccessful
        for prisioner in prisoners:
            if self.singlePrisonerAttemptingDraws(prisioner, shelfOfDrawers) == 0:
                return 0

        return 1

for i in range(0, 100):
    exp = PrisionExperiment()
    print (exp.performExperiment())
        

