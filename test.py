import unittest
from main import *


# Unit tests
def test_countUniqueNames():
    assert countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli") == 1
    assert countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli") == 1
    assert countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli") == 1
    assert countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah") == 1
    assert countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli") == 2
    assert countUniqueNames("Michele", "Egli", "Deborah", "Egli", "mohamed abraham Egli") == 3


test_countUniqueNames()
