import numpy as np
import numpy.typing as npt

from random import randint, shuffle

class PrisionExperiment:
    def __init__(self, numberOfPrisoners: int = 100, numberOFAttempts: int = 50) -> None:
        """
        Initializes the PrisonExperiment with the given number of prisoners and the allowed number of attempts.
        
        :param numberOfPrisoners: Total number of prisoners participating in the experiment. Default is 100.
        :param numberOfAttempts: Maximum number of attempts each prisoner is allowed to make. Default is 50.
        """
        self.numberOfPrisoners = numberOfPrisoners
        self.drawerAttenumberOFAttemptsmpts = numberOFAttempts


    @staticmethod
    def getRandomList(lenOfList) -> npt.NDArray:
        """
        Generates a shuffled list of numbers from 0 to lenOfList-1.
        
        :param lenOfList: Length of the list to be generated.
        :return: A shuffled numpy array of integers.
        """
        randomList = np.arange(0, lenOfList, dtype=int)
        shuffle(randomList)
        return randomList


    def singlePrisonerAttemptingDraws(self, prisioner: int, shelfOfDrawers: npt.NDArray) -> int:
        """
        Simulates a single prisoner attempting to find their number within the allowed number of attempts.
        
        :param prisoner: The number representing the prisoner.
        :param shelfOfDrawers: The shuffled array representing the drawers with hidden numbers.
        :return: 1 if the prisoner finds their number within the allowed attempts, otherwise 0.
        """
        drawerNumber = prisioner
        for attempt in range(0, self.numberOFAttempts):
            drawnNumber = shelfOfDrawers[drawerNumber]
            if drawnNumber == prisioner:
                return 1
            else:
                drawerNumber = drawnNumber
        return 0


    def performExperiment(self,) -> int:
        """
        Performs the prison experiment for all prisoners.
        
        :return: 1 if all prisoners are successful in finding their numbers, otherwise 0.
        """
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
        

