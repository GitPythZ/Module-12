import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results1 = {}
        cls.all_results2 = {}
        cls.all_results3 = {}
        cls.all_results_min_dist = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.runner2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.runner3 = runner_and_tournament.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results1)
        print(cls.all_results2)
        print(cls.all_results3)
        print(cls.all_results_min_dist)

    def test_tour_1(self):
        tour = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        call_def = tour.start()
        for keys, values in call_def.items():
            self.all_results1.update({keys: values.__str__()})
        self.assertTrue(call_def.get(2) == self.runner3)

    def test_tour_2(self):
        tour = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        call_def = tour.start()
        for keys, values in call_def.items():
            self.all_results2.update({keys: values.__str__()})
        self.assertTrue(call_def.get(2) == self.runner3)

    def test_tour_3(self):
        tour = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        call_def = tour.start()
        for keys, values in call_def.items():
            self.all_results3.update({keys: values.__str__()})
        self.assertTrue(call_def.get(3) == self.runner3)

    def test_tour_min_distance(self):
        tour = runner_and_tournament.Tournament(2, self.runner1, self.runner2, self.runner3)
        call_def = tour.start()
        for keys, values in call_def.items():
            self.all_results_min_dist.update({keys: values.__str__()})
        self.assertTrue(call_def.get(3) == self.runner3)
