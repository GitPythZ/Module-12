import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):

    IS_FROZEN = False

    @unittest.skipIf(IS_FROZEN, 'None')
    def test_walk(self):
        some_runner = runner_and_tournament.Runner('Bunny')
        for i in range(1, 11):
            some_runner.walk()
        self.assertEqual(some_runner.distance, 50)

    @unittest.skipIf(IS_FROZEN, 'None')
    def test_run(self):
        some_runner = runner_and_tournament.Runner('Bilbo')
        for i in range(1, 11):
            some_runner.run()
        self.assertEqual(some_runner.distance, 100)

    @unittest.skipIf(IS_FROZEN, 'None')
    def test_challenge(self):
        first_runner = runner_and_tournament.Runner('Joni')
        second_runner = runner_and_tournament.Runner('Hooks')
        for i in range(1, 11):
            first_runner.run()
        for i in range(1, 11):
            second_runner.walk()
        self.assertNotEqual(first_runner.distance, second_runner.distance)


class TournamentTest(unittest.TestCase):

    IS_FROZEN = True

    @classmethod
    def setUpClass(cls):
        cls.all_results1 = {}
        cls.all_results2 = {}
        cls.all_results3 = {}

    @unittest.skipIf(IS_FROZEN, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.runner2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.runner3 = runner_and_tournament.Runner('Ник', speed=3)

    # @classmethod
    # def tearDownClass(cls):
    #     print(cls.all_results1)
    #     print(cls.all_results2)
    #     print(cls.all_results3)

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