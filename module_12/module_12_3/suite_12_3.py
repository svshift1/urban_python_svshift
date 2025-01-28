import unittest
# from runner import *
from testRunner import RunnerTest
from testTournament import TournamentTest


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner=unittest.TextTestRunner(verbosity=2)
runner.run(suite)
