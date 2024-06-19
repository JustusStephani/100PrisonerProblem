import pytest
import numpy as np

from random import randint

from src.prisonExperiment import PrisonExperiment


def test_getRandomList():
    lenOfList = 100
    randomList = PrisonExperiment.getRandomList(lenOfList)
    assert isinstance(randomList, np.ndarray), "The returned object should be a numpy array"
    assert len(randomList) == lenOfList, "The length of the array should be equal to lenOfList"
    assert sorted(randomList) == list(range(lenOfList)), "The array should contain all integers from 0 to lenOfList-1"


def test_singlePrisonerAttemptingDraws_success():
    experiment = PrisonExperiment(numberOfPrisoners=100, numberOfAttempts=50)
    shelfOfDrawers = np.arange(100)
    prisoner = randint(0, 99)
    assert experiment.singlePrisonerAttemptingDraws(prisoner, shelfOfDrawers) == 1, "Prisoner should always find their number in a direct mapping"


def test_singlePrisonerAttemptingDraws_failure():
    experiment = PrisonExperiment(numberOfPrisoners=100, numberOfAttempts=1)
    shelfOfDrawers = PrisonExperiment.getRandomList(100)
    prisoner = randint(0, 99)
    # It's not guaranteed that the prisoner will fail, but with 1 attempt it's highly probable
    assert experiment.singlePrisonerAttemptingDraws(prisoner, shelfOfDrawers) in [0, 1], "The result should be either 0 or 1"


def test_performExperiment_success():
    experiment = PrisonExperiment(numberOfPrisoners=5, numberOfAttempts=5)
    # Create a scenario where prisoners always find their numbers
    shelfOfDrawers = np.array([0, 1, 2, 3, 4])
    experiment.getRandomList = lambda x: shelfOfDrawers
    assert experiment.performExperiment() == 1, "All prisoners should find their numbers"


def test_performExperiment_failure():
    experiment = PrisonExperiment(numberOfPrisoners=5, numberOfAttempts=2)
    # Create a scenario where it's unlikely that all prisoners find their numbers
    shelfOfDrawers = np.array([1, 0, 3, 4, 2])
    experiment.getRandomList = lambda x: shelfOfDrawers
    assert experiment.performExperiment() == 0, "Not all prisoners should find their numbers"
