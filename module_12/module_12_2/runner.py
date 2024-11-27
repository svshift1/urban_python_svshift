class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Runner("{self.name}", {self.speed})'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
        #№ если раскомментировать следующую строчку, то 4 тест пройдет   <------  !!!!!!!!!!!!!!!!
        #self.participants.sort(key=lambda x : x.speed, reverse=True)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    # ошибка тут -- более быстрый бегун может проиграть менее быстрому но стоящему ранее в списке
                    # если они финишируют в течение одной условной секунды
                    place += 1
                    self.participants.remove(participant)

        return finishers