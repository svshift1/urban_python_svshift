import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    def test_walk(self):
        r = Runner("vasya")
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    def test_run(self):
        r = Runner("vasya")
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    def test_challlenge(self):
        r1 = Runner('vasya')
        r2 = Runner('petya')
        for i in range(10):
            r1.walk()
            r1.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
