import unittest
from runner import Runner
import logging

# прошу понять и простить за выпендреж.

logger = logging.getLogger('')
def loggable(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            logger.info(f"тест {func.__name__} пройден успешно")
        except Exception as e:
            logger.warning(f"{func.__name__}  ошибка {type(e).__name__}:{str(e)}")
            # raise e # передать исключение дальше, чтобы pytest не считал его успешным ?
            RunnerTest().assertTrue(False) # костыль. чтобы тест считался проваленным
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    @loggable
    def test_walk(self):
        r = Runner("vasya", -5)
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    @loggable
    def test_run(self):
        r = Runner(["vasya"])
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, "Все тесты в этом классе заморожены")
    @loggable
    def test_challlenge(self):
        r1 = Runner('vasya')
        r2 = Runner('petya')
        for i in range(10):
            r1.walk()
            r1.run()
        self.assertNotEqual(r1.distance, r2.distance)

