import unittest
import runner


class TournamentTest(unittest.TestCase):

    allres=list()
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        TournamentTest.allres = []

    def setUp(self):
        self.wusein = runner.Runner('Усейн',10)
        self.andrey = runner.Runner('Андрей',9)
        self.nik = runner.Runner('Nick',3)
        #print(self.wusein, self.andrey, self.nik)

    def test_run1(self):
        t = runner.Tournament(90, self.wusein, self.nik)
        res = t.start()
        self.assertTrue(res[1] == self.wusein and res[2] == self.nik)
        TournamentTest.allres.append(res)

    def test_run2(self):
        t = runner.Tournament(90, self.andrey, self.nik)
        res = t.start()
        self.assertTrue(res[1] == self.andrey and res[2] == self.nik)
        TournamentTest.allres.append(res)


    def test_run3(self):
        t = runner.Tournament(90, self.wusein, self.andrey, self.nik)
        # вот так сработал бы и оригинальный вариант
        #  t = runner.Tournament(90, self.wusein, self.andrey, self.nik)
        res = t.start()
        TournamentTest.allres.append(res)
        self.assertTrue(res[2] == self.andrey and res[1] == self.wusein and res[3] == self.nik)
        TournamentTest.allres.append(res)



    # переставим местами слагаемые, и упс -- вот но, доп условие!
    # рецепт лечения в комментаиях Tournament.__init__
    def test_run4_fail(self):
        t = runner.Tournament(90, self.andrey, self.wusein, self.nik)
        # вот так сработал бы и оригинальный вариант
        #  t = runner.Tournament(90, self.wusein, self.andrey, self.nik)
        res = t.start()
        TournamentTest.allres.append(res)
        self.assertTrue(res[2] == self.andrey and res[1] == self.wusein and res[3] == self.nik)
        TournamentTest.allres.append(res)

    @classmethod
    def tearDownClass(slc):
        print('')
        for r in TournamentTest.allres:
            print(str(r))

if __name__=='__main__':
    unittest.main()

