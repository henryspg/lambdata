import unittest
import lambdata_henry as lh

class LambdataHenryTests(unittest.TestCase):
    def test_state_to_abbr(self):
        abbr_alaska = lh.StateAbbreviation().get_abbreviation_from_state("Alaska")
        self.assertEqual(abbr_alaska, "AK")


    def test_abbr_to_state(self):
        texas_abbr = lh.StateAbbreviation().get_state_from_abbreviation("TX")
        self.assertEqual(texas_abbr, "Texas")



if __name__ == '__main__':
    unittest.main()