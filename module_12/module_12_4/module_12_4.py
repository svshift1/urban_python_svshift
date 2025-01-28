import unittest
import logging
from runner import Runner
from testRunner import RunnerTest


#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, encoding="utf-8", filename="runner_test.log", filemode='w',
                    format="%(asctime)s|%(levelname)s| %(message)s")

# это забавно, но аннотатор  @loggable который я написал устроен так, что все тесты проходят.
# пришлось в него вставить костыль чтобы при непойманном исключении было бы fail
# не знаю правильно ли это
unittest.main(verbosity=2)