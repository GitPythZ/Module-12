import unittest
import runner_test


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        any_walker = runner_test.Runner("Gamp")
        for i in range(1, 11):
            any_walker.walk()
        self.assertEqual(any_walker.distance, 50)

    def test_run(self):
        any_runner = runner_test.Runner("Ridley Scott")
        for i in range(1, 11):
            any_runner.run()
        self.assertEqual(any_runner.distance, 100)

    def test_challenge(self):

