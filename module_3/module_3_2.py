#from regex import fullmatch


#   с только-позиционными параметрами даже интереснее:
#   def send_mail(txt: str, receiver: str, /, sender='university.help@gmail.com') -> None:
def send_email(txt: str, recipient: str, *, sender: str = 'university.help@gmail.com') -> None:
    if not is_addr(recipient) or not is_addr(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


def is_addr(addr: str) -> bool:
    # проверял что тоже работае:
    # return fullmatch(r'.*@.*(\.com|\.ru|\.net)$', addr) is not None
    return '@' in addr and \
        (addr.endswith('.com') or addr.endswith('.ru') or addr.endswith('.net'))


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# а так -- ошибка )
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')

