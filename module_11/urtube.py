#needed for module_11_3

import time
from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: (int, float)):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

    def __repr__(self):
        return f"User('{self.nickname}',{self.age})"
    def __eq__(self,other: {str, 'User'}):
        if isinstance(other, User):
            return other.nickname.lower()==self.nickname.lower()
        elif isinstance(other, str):
            return other.lower() == self.nickname.lower()
        else:
            return False


class Video:

    def __init__(self, title: str, duration: (int, float), adult_mode: bool = False):
        self.title: str = title
        self.duration: float = duration
        self.adult_mode: bool = adult_mode
        self.time_now: float = 0

    def __str__(self):
        return f"'{self.title}'"

    def __repr__(self):
        return f"Video(title='{self.title}', duration={self.duration}, { '18+' if  self.adult_mode else ''})"

    def __eq__(self, other: (str, 'Video')):
        if isinstance(other, str):
            return self.title.lower() == other.lower()
        elif isinstance(other, Video):
            return self.title.lower() == other.title.lower()
        else:
            return False

    def __contains__(self, patt: str) -> bool:
        return patt.lower() in self.title.lower()


class UrTube:

    def __init__(self):
        self.users: list = []
        self.videos: list = []
        self.current_user: User = None

    def log_in(self, nickname: str, password: str) -> bool:
        if nickname not in self.users:
            print(f"Пользователь {nickname} не найден")
            return False
        u: User = self.users[self.users.index(nickname)]
        if u.password==hash(password):
            self.current_user=u
            return True
        print(f"Пароль для {nickname} не подходит")
        return False

    def register(self, nickname: str, password: str, age: (int, float)) -> None:
        u = User(nickname, hash(password), age)
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
            return
        self.users.append(u)
        self.current_user = u

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *videos) -> None:
        for v in videos:
            if v not in self.videos:
                # print('added',v)
                self.videos.append(v)
            # else:
            #     print('фильм', v, 'уже есть')

    def get_videos(self, patt: str) -> list:
        return [v.title for v in self.videos if patt in v]

    def watch_video(self, title: str) -> bool:
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return False
        v = next((it for it in self.videos if it==title),None)
        if v is None:
            # print(f"Видео '{title}' не найдено")
            return False

        if v.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return False
        for t in range(1,v.duration+1):
            v.current_time=t
            print(f"{v.current_time} ", end="")
            time.sleep(1.0)
        print("Конец Видео")
        return True


if __name__=='__main__':

    ur = UrTube()

    v1 = Video('Самый худший фильм', 200)
    v15 = Video('самый худший фильм', 200)
    v2 = Video('Для чего девушкам парень?', 10, adult_mode=True)
    ur.add(v1, v15, v2)

    ur.register('anonymous','123456789',422)
    ur.log_out()
    ur.log_in('somebody','pass')
    ur.log_in('anonymous','987654321')
    ur.log_in('anonymous','123456789')
    ur.log_out()

    print("-----------------------")

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
